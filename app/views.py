from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Product, Order, Cart #Add additional classes to be imported here later
from .serializers import ProductSerializer, OrderSerializer, CartSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')#or by 'id' or 'category'
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_id')
    serializer_class = OrderSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all().order_by('cart_id')#or by 'id' or 'category'
    serializer_class = CartSerializer

'''
class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class OrderListView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
'''