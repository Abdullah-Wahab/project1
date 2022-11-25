from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.db.models import Max
from .models import Shop, Supplier, Order
from .serializers import ShopSerializer, SupplierSerializer, OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter


# Create your views here.

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'supplier__name', 'address', 'phone']
    ordering_fields = ['id', 'name', 'supplier']


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['^name']
    ordering_fields = ['name', 'shop_detail']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['supplier__name', 'shop__name']
    ordering_fields = ['quantity', 'supplier__name', 'shop__name', 'material']
