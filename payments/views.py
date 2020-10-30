from django.conf import settings
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


import stripe


def success(request):

    return render(request, 'payments/success.html')


def cancelled(request):

    return render(request, 'payments/cancelled.html')


def payment(request):

    return render(request, 'payment.html')


@csrf_exempt
def checkout(request):

    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        items_id=[{
            "price": 'grand_total',
            "quantity": 1,
            }],
        mode="payment",
        success_url=request.build_absolute_uri(reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=request(reverse('payment')),
    )

    JsonResponse({
        'session_id': session.id,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })
