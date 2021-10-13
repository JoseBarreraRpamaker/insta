from django.shortcuts import render

from django.contrib.auth import authenticate, default_app_config , login    
from django.shortcuts import render


def login_views(request):
    return render(request,'users/login.html')
