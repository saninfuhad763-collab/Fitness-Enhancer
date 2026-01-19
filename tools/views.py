

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.models import UserProfile
from django.http import HttpResponseForbidden
from users.utils import is_premium

@login_required
def calorie_calculator(request):

    if not is_premium(request.user):
        return HttpResponseForbidden(
            "Upgrade to Premium to use the calorie calculator"
        )

    return render(request, 'tools/calorie_calculator.html')

    profile = UserProfile.objects.get(user=request.user)

    # BMR calculation (Mifflin-St Jeor)
    bmr = (10 * profile.weight) + (6.25 * profile.height) - (5 * profile.age) + 5

    # Activity factor
    activity_factor = 1.4 if profile.experience == 'beginner' else 1.6
    tdee = bmr * activity_factor

    # Goal-based calorie adjustment
    if profile.goal == 'fat_loss':
        calories = tdee - 500
        protein = profile.weight * 1.6
    elif profile.goal == 'lean':
        calories = tdee + 300
        protein = profile.weight * 2.0
    else:
        calories = tdee
        protein = profile.weight * 1.4

    context = {
        'bmr': round(bmr),
        'tdee': round(tdee),
        'calories': round(calories),
        'protein': round(protein, 1),
    }

    return render(request, 'tools/calorie.html', context)