from rest_framework import serializers
from .models import Shop, Supplier, Order


class OrderSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['material', 'quantity']


class ShopSerializer(serializers.ModelSerializer):
    orders = OrderSerializer1(many=True, read_only=True, source='order_set')
    supplier = serializers.SlugRelatedField(slug_field='name', queryset=Supplier.objects.all())

    class Meta:
        model = Shop
        fields = ['id', 'name', 'address', 'supplier', 'orders']


class SupplierSerializer(serializers.ModelSerializer):
    shop_detail = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Supplier
        Supplier.objects.order_by('shop_detail')
        fields = ['id', 'name', 'address', 'shop_detail']


class OrderSerializer(serializers.ModelSerializer):
    shop = serializers.SlugRelatedField(slug_field='name', queryset=Shop.objects.all())
    supplier = serializers.SlugRelatedField(slug_field='name', queryset=Supplier.objects.all())

    class Meta:
        model = Order
        fields = ['supplier', 'material', 'quantity', 'shop']
