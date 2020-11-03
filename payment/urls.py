from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('cache_payment_data/', views.cache_payment_data, name='cache_payment_data'),
]
