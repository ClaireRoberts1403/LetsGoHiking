from django.conf import settings
from django.shortcuts import render
from django.urls import reverse


import stripe


def success(request):

    return render(request, 'payments/success.html')


def cancelled(request):

    return render(request, 'payments/cancelled.html')


def payment(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        items_id=[{
            "price": 'price_1HgYVJBr9rDAn4pHQED1F69Q',
            "quantity": 1,
            }],
        mode="payment",
        success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request(reverse('payment')),
    )

    context = {
        'session_id': session.id,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    }
    return render(request, 'payment.html', context)
