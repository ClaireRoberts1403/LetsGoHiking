from django.shortcuts import render
from .models import product


def products(request):
    products = product.objects.all()

    return render(request, 'shop/shop.html', {'products': products})
