from django.urls import path
from .views import generate_workout, weekly_schedule

urlpatterns = [
    path('', generate_workout, name='workout_plan'),
    path('weekly/', weekly_schedule, name='weekly_schedule'),
]
