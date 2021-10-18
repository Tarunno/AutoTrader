from django.urls import path
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/', views.car, name='car'),
    path('place-bid/<int:car_id>/', views.place_bid, name='place-bid'),
]
