from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    current_datetime = timezone.localtime(timezone.now())
    cars = Car.objects.filter(end_at__gte=current_datetime).order_by('end_at')
    removed_car = Car.objects.filter(end_at__lt=current_datetime)
    for i in removed_car:
        i.on_auction = False
        i.save()

    if request.GET.get('make'):
        if request.GET.get('make') != 'All':
            cars = cars.filter(make=request.GET.get('make'))
    if request.GET.get('transmission'):
        if request.GET.get('transmission') != 'All':
            cars = cars.filter(transmission=request.GET.get('transmission'))
    if request.GET.get('body_style'):
        if request.GET.get('body_style') != 'All':
            cars = cars.filter(body_style=request.GET.get('body_style'))

    images = []
    for car in cars:
        image = Photo.objects.filter(car=car).first()
        images.append(image)
        car.time = (car.end_at - current_datetime).total_seconds()

    context = {
        'cars': cars,
    }
    return render(request, 'app/home.html', context)

def car(request, id):
    car = Car.objects.get(id=id)
    current_datetime = timezone.localtime(timezone.now())
    removed_car = Car.objects.filter(end_at__lt=current_datetime)
    car.time = (car.end_at - current_datetime).total_seconds()
    for i in removed_car:
        i.on_auction = False
        i.save()
    context = {
        'car': car
    }
    return render(request, 'app/car.html', context)


@login_required
def place_bid(request, car_id):
    car = Car.objects.get(id=car_id)
    current_datetime = timezone.localtime(timezone.now())
    removed_car = Car.objects.filter(end_at__lt=current_datetime)
    car.time = (car.end_at - current_datetime).total_seconds()
    context = {
        'car': car
    }
    for i in removed_car:
        i.on_auction = False
        i.save()
    if request.method == "POST":
        if car.on_auction:
            if car.seller == request.user:
                return JsonResponse({'error': "Can't bid your own car!"}, safe=False)
            bid_value = request.POST.get('bid_value')
            car.bid = bid_value
            car.save()
            return JsonResponse({'success': 'Bid placed!'}, safe=False)
        else:
            return JsonResponse({'error': 'No longer on auction!'}, safe=False)
    return render(request, 'app/bid.html', context)

@login_required
def remove_bid(request, car_id):
    car = Car.objects.get(id=car_id)
    car.on_auction = False 
    car.save()
    return JsonResponse({'car_id': car_id}, safe=False)