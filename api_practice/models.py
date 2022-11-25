from django.db import models


# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.name, self.address)


class Shop(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name='shop_detail')

    def __str__(self):
        return '%s %s' % (self.name, self.address)


class Order(models.Model):
    Items = (('egg', 'EGG'), ('juice', 'JUICE'), ('milk', 'MILK'), ('bread', 'BREAD'), ('butter', 'BUTTER'))
    material = models.CharField(choices=Items, max_length=10, default='egg')
    quantity = models.IntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    shop = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'Order From -> ' + str(self.supplier) + ' -- For Shop -> ' + str(self.shop)
