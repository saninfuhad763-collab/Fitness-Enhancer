from django import forms
from .models import WeightProgress

class WeightProgressForm(forms.ModelForm):
    class Meta:
        model = WeightProgress
        fields = ['weight', 'note']