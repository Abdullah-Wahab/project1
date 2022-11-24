from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User, Shop, Supplier, Order
from .serializers import UserSerializer, ShopSerializer, SupplierSerializer, OrderSerializer
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.

# @csrf_exempt
# def shop_list(request):
#     """
#     List all shop list, or create a shop.
#     """
#     if request.method == 'GET':
#         snippets = Shop.objects.all()
#         serializer = ShopSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ShopSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


class ShopViewSet(viewsets.ViewSet):
    def list(self, request):
        sh = Shop.objects.all()
        serializer = ShopSerializer(sh, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        sh = Shop.objects.all()
        serializer = ShopSerializer(sh, many=True)
        return Response(serializer.data)


class SupplierViewSet(viewsets.ViewSet):
    def list(self, request):
        supplier = Shop.objects.all()
        serializer = ShopSerializer(supplier, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ViewSet):
    def list(self, request):
        order = Shop.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        user = Shop.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)