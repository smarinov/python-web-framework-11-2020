from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect


# Create your views here.
def login_view(request):
    username = 'smari'
    password = '12345qwe'
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return redirect('index')

    return redirect('index')


def logout_view(request):
    logout(request)
    return redirect('index')
