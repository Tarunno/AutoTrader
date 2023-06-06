from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from django.utils import timezone


def home(request):
    current_datetime = timezone.now()
    cars = Car.objects.filter(end_at__gte=current_datetime)
    removed_car = Car.objects.filter(end_at__lt=current_datetime)
    for car in removed_car:
        car.on_auction = False
        car.save()
    images = []
    for car in cars:
        image = Photo.objects.filter(car=car).first()
        images.append(image)
    context = {
        'cars': cars,
        'images': images
    }
    return render(request, 'app/home.html', context)

def car(request, id):
    car = Car.objects.get(id=id)
    current_datetime = timezone.now()
    removed_car = Car.objects.filter(end_at__lt=current_datetime)
    for car in removed_car:
        car.on_auction = False
        car.save()
    context = {
        'car': car
    }
    return render(request, 'app/car.html', context)

def place_bid(request, car_id):
    car = Car.objects.get(id=car_id)
    current_datetime = timezone.now()
    removed_car = Car.objects.filter(end_at__lt=current_datetime)
    context = {
        'car': car
    }
    for car in removed_car:
        car.on_auction = False
        car.save()
    if request.method == "POST":
        if car.on_auction:
            bid_value = request.POST.get('bid_value')
            car.bid = bid_value
            car.save()
            return JsonResponse({'success': 'Bid placed!'}, safe=False)
        else:
            return JsonResponse({'error': 'No longer on auction!'}, safe=False)
    return render(request, 'app/bid.html', context)
