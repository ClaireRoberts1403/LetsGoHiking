from django.shortcuts import render, redirect, reverse
from .models import product, category
from .forms import productForm


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


def add_product(request):

    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_product'))
    else:
        form = productForm()

    form = productForm()
    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
