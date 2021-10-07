from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def car(request):
    return render(request, 'app/car.html')
