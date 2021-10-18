from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def car(request):
    return render(request, 'app/car.html')

def place_bid(request, car_id):
    print(car_id)
    return render(request, 'app/bid.html')
