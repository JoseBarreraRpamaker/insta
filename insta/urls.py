"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path , include
from django.http import HttpResponse
from users import views as users_views


def hola_mundo(request):
    return HttpResponse("hola como estan")


urlpatterns = [
     path('admin/', admin.site.urls),
     path('hola/',hola_mundo),
     path('users/login/', users_views.login_view, name='login'),
     path('users/signup/', users_views.signup, name='signup'),
     path('',include('posts.urls')),


     
    
      

]


