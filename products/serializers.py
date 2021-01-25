from rest_framework import serializers

from .models import Products, Service, Product


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['itemID','itemName','itemPrice']
        

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['itemID','itemName','itemPrice']