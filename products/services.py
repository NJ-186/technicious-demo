from .models import Service, Product


def getServices():
    services = Service.objects.all()
    return services


def getProducts():
    products = Product.objects.all()
    return products