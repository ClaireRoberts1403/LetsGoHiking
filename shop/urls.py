from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('add_product/', views.add_product, name='add_product'),
]
