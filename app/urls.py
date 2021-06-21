from django.urls import path
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path('home/', views.home, name='home')
]
