from django.db import models

#Managers begin here

class ServiceManager(models.Manager):

    def get_queryset(self):
        return super(ServiceManager, self).get_queryset().filter(
            itemType = 'service')


class ProductManager(models.Manager):

    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(
            itemType = 'product')