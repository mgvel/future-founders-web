from django.urls import path
from . import views
app_name = 'store'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart-add'),
    path('cart/update/', views.cart_update, name='cart-update'),
    path('checkout/', views.checkout_view, name='checkout'),
]