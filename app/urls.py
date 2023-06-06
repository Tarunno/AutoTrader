from django.urls import path
from django.contrib.auth.models import User
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:id>/', views.car, name='car'),
    path('place-bid/<int:car_id>/', views.place_bid, name='place-bid'),
    path('remove-bid/<int:car_id>/', views.remove_bid, name='remove-bid'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
