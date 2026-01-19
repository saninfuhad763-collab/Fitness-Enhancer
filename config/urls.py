"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as auth_views

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # Auth URLs
    path(
        'users/login/',
        auth_views.LoginView.as_view(template_name='auth/login.html'),
        name='login'
    ),
    path(
        'users/logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path('users/', include('users.urls')),

    path('workout/', include('workouts.urls')),

    path('tools/', include('tools.urls')),

    path('progress/', include('progress.urls')),
]
