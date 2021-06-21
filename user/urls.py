from django.urls import path
from django.contrib.auth.models import User
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin')
]
