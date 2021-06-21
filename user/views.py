from django.shortcuts import render

def signup(request):
    return render(request, 'user/signup.html')


def signin(request):
    return render(request, 'user/signin.html')
