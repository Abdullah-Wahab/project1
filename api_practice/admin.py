from django.contrib import admin
from .models import Shop, Supplier, Order


# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'supplier']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'material', 'quantity', 'shop']
