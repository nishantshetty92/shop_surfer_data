from rest_framework.serializers import ModelSerializer
from shop.models import Category, Product, Cart, CartItem, Order, OrderItem, ShippingAddress
from rest_framework import serializers


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'is_selected']
        # read_only_fields = ['id']

#     # def create(self, validated_data):
#     #     product_data = validated_data.pop('product')
#     #     product = Product.objects.create(**product_data)
#     #     cart_item = CartItem.objects.create(product=product, **validated_data)
#     #     return cart_item

#     # def update(self, instance, validated_data):
#     #     product_data = validated_data.pop('product', None)
#     #     if product_data:
#     #         product = instance.product
#     #         for attr, value in product_data.items():
#     #             setattr(product, attr, value)
#     #         product.save()
#     #     instance.quantity = validated_data.get('quantity', instance.quantity)
#     #     instance.save()
#     #     return instance
    
#     # def partial_update(self, instance, validated_data):
#     #     return self.update(instance, validated_data)

class OrderProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class OrderItemSerializer(serializers.ModelSerializer):
    # product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    product_name = serializers.SerializerMethodField()
    product_slug = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['product_id', 'product_name', 'product_slug', 'price', 'quantity']

    def get_product_name(self, obj):
        return obj.product.name if obj.product.name else None
    
    def get_product_slug(self, obj):
        return obj.product.slug if obj.product.slug else None

class OrderSerializer(ModelSerializer):
    # order_items = OrderItemSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(format='%d %B %Y')

    class Meta:
        model = Order
        fields = ['order_id', 'total_amount', 'created_at', 'shipping_address', 'payment_method']

class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['id', 'full_name', 'mobile_number', 'pin_code', 'address1', 'address2', 'city', 'state', 'is_default']
