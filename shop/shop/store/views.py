from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.db import transaction
from .models import Product, Order, OrderItem
from .forms import AddToCartForm


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    paginate_by = 12
    queryset = Product.objects.filter(active=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = AddToCartForm()
        return ctx


# Session-based cart helpers
CART_SESSION_KEY = 'cart'


def _get_cart(request):
    return request.session.setdefault(CART_SESSION_KEY, {})


def cart_add(request, product_id):
    product = get_object_or_404(Product, pk=product_id, active=True)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            qty = form.cleaned_data['quantity']
        else:
            qty = 1
    else:
        qty = 1

    cart = _get_cart(request)
    pid = str(product_id)
    item = cart.get(pid, {'quantity': 0, 'price': str(product.price), 'name': product.name})
    item['quantity'] = int(item.get('quantity', 0)) + int(qty)
    cart[pid] = item
    request.session.modified = True
    return redirect('store:cart')


def cart_view(request):
    cart = _get_cart(request)
    items = []
    total = 0
    for pid, data in cart.items():
        total += int(data['quantity']) * float(data['price'])
        items.append({'product_id': pid, **data})
    return render(request, 'store/cart.html', {'items': items, 'total': total})


def cart_update(request):
    # expects POST with quantities like quantities-<product_id>
    if request.method == 'POST':
        cart = _get_cart(request)
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                pid = key.split('quantity_')[1]
                try:
                    qty = int(value)
                except (ValueError, TypeError):
                    qty = 0
                if qty <= 0:
                    cart.pop(pid, None)
                else:
                    if pid in cart:
                        cart[pid]['quantity'] = qty
        request.session.modified = True
    return redirect('store:cart')


@transaction.atomic
def checkout_view(request):
    cart = _get_cart(request)
    if not cart:
        return redirect('store:product-list')

    # create order
    order = Order.objects.create(user=request.user if request.user.is_authenticated else None)
    for pid, data in cart.items():
        OrderItem.objects.create(
            order=order,
            product_id=int(pid),
            quantity=int(data['quantity']),
            price=data['price']
        )
    # clear cart
    request.session[CART_SESSION_KEY] = {}
    request.session.modified = True

    # In production: integrate with Stripe/PayPal and webhooks
    return render(request, 'store/checkout_success.html', {'order': order})