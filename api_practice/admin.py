from django.contrib import admin
from .models import User, Shop, Supplier, Order


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Shop)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']


@admin.register(Supplier)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']


@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'materials', 'quantity', 'shop']
