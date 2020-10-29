from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('my_challenges/', views.my_challenges, name='my_challenges'),
    path('my_order_history', views.my_order_history, name='my_order_history'),
     path('submit_idea', views.submit_idea, name='submit_idea'),
]
