from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserRegistrationForm(UserCreationForm):
    age = forms.IntegerField()
    height = forms.FloatField(help_text="Height in cm")
    weight = forms.FloatField(help_text="Weight in kg")
    goal = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
            'age',
            'height',
            'weight',
            'goal',
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'height', 'weight', 'goal', 'experience']