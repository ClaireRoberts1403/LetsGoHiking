from django.shortcuts import render
from .models import product


def shop(request):
    products = product.objects.all()

    return render(request, 'shop/shop.html', {'products': products})
