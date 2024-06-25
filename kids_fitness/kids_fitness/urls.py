"""
URL configuration for kids_fitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .settings import MEDIA_ROOT, MEDIA_URL, DEBUG
from django.conf.urls.static import static
from kids_fitness_app.views import *


urlpatterns = [
    path('', main, name='main'),
    path('about/', about_us, name='about_us'),
    path('gallery/', gallery, name='gallery'),
    path('contacts/', contacts, name='contacts'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('service/', service, name='service'),
    path('sign_up/', sign_up, name='sign_up'),
    path('send-mails/', send_mails, name='send_mails'),
    path('submit_registration/', submit_registration, name='submit_registration'),
]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)