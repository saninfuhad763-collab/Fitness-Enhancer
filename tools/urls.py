from django.urls import path
from .views import calorie_calculator

urlpatterns = [
    path('calories/', calorie_calculator, name='calorie_calculator'),
]