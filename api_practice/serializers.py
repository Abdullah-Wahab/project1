from rest_framework import serializers
from .models import Shop, Supplier, Order


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'phone']


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'address']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['supplier', 'materials', 'quantity', 'shop']
