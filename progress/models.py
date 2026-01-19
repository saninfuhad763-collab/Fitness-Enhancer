

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class WeightProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField(help_text="Weight in kg")
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg"