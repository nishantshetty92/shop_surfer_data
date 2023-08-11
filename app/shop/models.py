from django.db import models
from django.conf import settings
import uuid
from datetime import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ManyToManyField(Category, through='ProductCategory', related_name='products')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.JSONField(null=True, blank=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    fast_delivery = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    quantity = models.IntegerField(default=10)
    seller = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    
class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['product', 'category']

    def __str__(self):
        return f"{self.category.id}_{self.product.slug}"
    
class TopCategory(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    total_purchases = models.IntegerField(default=0)

    def __str__(self):
        return str(self.category.id)
    
class Cart(models.Model):
    user_id = models.IntegerField(unique=True)
    cart_items = models.ManyToManyField(Product, through='CartItem', related_name='cart_items')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_id)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    is_selected = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['cart', 'product']

    def __str__(self):
        return "{}_{}".format(self.cart.user_id, self.id)

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.IntegerField()
    order_items = models.ManyToManyField(Product, through='OrderItem', related_name='order_items')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return str(self.order_id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['order', 'product']

    def __str__(self):
        return f"{str(self.order_id)}_{self.product.id}"

class ShippingAddress(models.Model):
    user_id = models.IntegerField()
    full_name = models.CharField(max_length=150, blank=True)
    mobile_number = models.CharField(max_length = 10)
    pin_code = models.CharField(max_length = 10)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=150, blank=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id}_{self.full_name}"
