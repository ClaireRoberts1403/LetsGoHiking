from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from shop.models import Product


def cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def update_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Deleted {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def delete_from_cart(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart.pop(item_id)
        messages.success(request, f'Deleted {product.name} from your cart')
    else:
        messages.success(request, f'Could not delete {product.name} from your cart')

    request.session['cart'] = cart
    return HttpResponse(status=200)
