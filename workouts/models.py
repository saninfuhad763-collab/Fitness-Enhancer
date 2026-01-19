

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    title = models.CharField(max_length=100)
    goal = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.title


class WeeklyWorkout(models.Model):
    DAYS = [
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=3, choices=DAYS)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.get_day_display()}"