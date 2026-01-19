

# Register your models here.
from django.contrib import admin
from .models import Exercise, WorkoutPlan, WeeklyWorkout

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(WeeklyWorkout)