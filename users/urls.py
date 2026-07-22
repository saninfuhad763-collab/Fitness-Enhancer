from django.urls import path
from .views import register, dashboard, upgrade, edit_profile

urlpatterns = [
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('upgrade/', upgrade, name='upgrade'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]