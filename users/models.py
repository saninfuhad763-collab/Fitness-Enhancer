from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")



    GOAL_CHOICES = [
        ('fat_loss', 'Fat Loss'),
        ('lean_muscle', 'Lean Muscle'),
        ('fitness', 'General Fitness'),
    ]

    goal = models.CharField(max_length=100, choices=GOAL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    LEVEL_CHOICES = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ]

    

    experience = models.CharField(
    max_length=20,
    choices=LEVEL_CHOICES,
    default='beginner'
)

    def __str__(self):
        return self.user.username
    


class Subscription(models.Model):
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default='free')
    start_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.plan}"    