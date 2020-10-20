from django.shortcuts import render
from .models import product, category


def shop(request):
    products = product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)

    context = {
        'products': products,
        'current_categories': categories,
    }

    return render(request, 'shop/shop.html', context)
