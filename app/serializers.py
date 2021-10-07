from rest_framework import serializers

from .models import Product,  Order, Cart
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'description')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id', 'address','customer_id', 'payment')


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('cart_id', 'cart_name', 'cart_price', 'cart_category', 'cart_description')