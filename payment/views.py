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
        'stripe_public_key': 'pk_test_51HZDumBr9rDAn4pHhR9viH3NbBYSif3xmLDYkpWkP3trKnCPiP9ZnhwuXpZTjJVau7qRB7bIIy8H1PhlAShE06fu00OEmLsz6Q',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
