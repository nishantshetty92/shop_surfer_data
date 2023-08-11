from django.contrib import admin
from shop.models import Category, Product, ProductCategory, TopCategory, Cart, CartItem, Order, OrderItem, ShippingAddress


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(TopCategory)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)