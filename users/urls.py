from django.urls import path
from .views import register, dashboard, upgrade

urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('upgrade/', upgrade, name='upgrade'),
    
]