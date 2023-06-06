from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.models import User
from .forms import *
from app.models import *
from .models import *
import json

def signup(request):
    form = UserSignup(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "success"}, safe=True)
        else:
            error = form.errors
            return JsonResponse({"message": error}, safe=True)
    context = {
        "title": "Sign Up"
    }
    return render(request, 'user/signup.html', context)


def signin(request):
    form = UserSignin(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(request)
            print(request.user.id)
            return JsonResponse({"message": "success", "userID": request.user.id}, safe=True)
        else:
            error = form.errors
            return JsonResponse({"message": error}, safe=True)
    context = {
        'title': 'Sign in'
    }
    return render(request, 'user/signin.html', context)

@login_required
def profile(request, userID):
    user = User.objects.get(id=userID)
    cars = Car.objects.filter(seller=request.user).order_by('-end_at')[0:2]
    customer = user.customer
    context = {
        'title': 'Profile',
        'user': user,
        'cars':cars,
        'customer': customer
    }
    return render(request, 'user/profile.html', context)

@login_required
def add_car(request):
    if request.method == 'POST':
        car = Car.objects.create(
            make = request.POST.get('make'),
            model = request.POST.get('model'),
            seller = request.user,
            location = request.POST.get('location'),
            vin = request.POST.get('vin'),
            mileage = request.POST.get('mileage'),
            body_style = request.POST.get('body_style'),
            engine = request.POST.get('engine'),
            drivetrain = request.POST.get('drivetrain'),
            transmission = request.POST.get('transmission'),
            transmission_speed = int(request.POST.get('transmission_speed')),
            exterior_color = request.POST.get('exterior_color'),
            interior_color = request.POST.get('interior_color'),
            title_status = request.POST.get('title_status'),
            seller_type = request.POST.get('seller_type'),
            highlight = request.POST.get('highlight'),
            equipment = request.POST.get('equipment'),
            modification = request.POST.get('modification'),
            known_flaw = request.POST.get('known_flaw'),
            recent_service_history = request.POST.get('recent_service_history'),
            ownership_history = request.POST.get('ownership_history'),
            seller_note = request.POST.get('seller_note'),
            end_at = request.POST.get('end_at')
        )
        car = Car.objects.get(id=car.id)
        exterior_images = request.FILES.getlist('exterior_images')
        for image in exterior_images:
            Photo.objects.create(car=car, image=image, type="Exterior")
        interior_images = request.FILES.getlist('interior_images')
        for image in interior_images:
            Photo.objects.create(car=car, image=image, type="Interior")
        customer = Customer.objects.get(user=request.user)
        customer.auction_posted = customer.auction_posted + 1
        customer.save()
        return JsonResponse({'POST': 'success'}, safe=True)
    else:
        return JsonResponse({'error': 'invalid request'}, safe=True)
