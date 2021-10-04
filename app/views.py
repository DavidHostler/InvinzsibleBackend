from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Product, Order #Add additional classes to be imported here later
from .serializers import ProductSerializer, OrderSerializer

from rest_framework.generics import ListAPIView, RetrieveAPIView
'''
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')#or by 'id' or 'category'
    serializer_class = ProductSerializer

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
