from django.contrib import admin
from .models import Category, Product, ProductImage, Order, OrderItem

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "active")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]

admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

