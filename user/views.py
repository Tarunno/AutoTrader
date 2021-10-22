from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .forms import *
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
            form.save()
            return JsonResponse({"message": "success"}, safe=True) 
    context = {
        'title': 'Sign in'
    }
    return render(request, 'user/signin.html')
