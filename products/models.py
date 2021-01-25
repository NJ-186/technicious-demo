from django.db import models
from .manager import ServiceManager, ProductManager

# Create your models here.

class Products(models.Model):
    itemID = models.CharField(
        primary_key = True,
        default = '',
        max_length = 10,
    )
    itemName = models.CharField(
        max_length = 30,
        unique = True,
        default = 'product 1'
    )
    itemPrice = models.FloatField()
    
    item_choices = (
        ('service','service'),
        ('product','product')
    )

    itemType = models.CharField(
        default = 'product',
        max_length = 7,
        choices = item_choices
    )

    class Meta:
        verbose_name = 'products'

    def __str__(self):
        return self.itemID + " - " + self.itemName


class Service(Products):
    objects = ServiceManager()

    class Meta:
        proxy = True


class Product(Products):
    objects = ProductManager()

    class Meta:
        proxy = True