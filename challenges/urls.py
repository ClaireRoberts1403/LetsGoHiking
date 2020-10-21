from django.urls import path
from . import views


urlpatterns = [
    path('', views.challenges, name='challenges'),
    path('add/', views.add_challenge, name='add_challenge'),
    path('full_challenge/', views.full_challenge, name='full_challenge'),
]
