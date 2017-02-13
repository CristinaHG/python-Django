from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.

def login(request):
    pass


def logout(request):
    if request.user.is_authenticated():
        logout(request)
    return redirect('photos_home')

