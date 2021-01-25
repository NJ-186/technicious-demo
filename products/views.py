from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ServiceSerializer, ProductSerializer
from .services import getProducts, getServices

# Create your views here.

@api_view(['GET'])
def home(request):
    api_urls = {
        'Get All Services':'getAllServices',
        'Get All Products':'getAllProducts',
    }
    return Response(api_urls)


@api_view(['GET'])
def getAllServices(request):
    services = getServices()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(['GET'])
def getAllProducts(request):
    products = getProducts()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)