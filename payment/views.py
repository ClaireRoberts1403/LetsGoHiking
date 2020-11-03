from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt


def payment(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('shop'))

    order_form = OrderForm()
    template = 'payment/payment.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
