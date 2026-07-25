from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from users.models import UserProfile
from users.utils import is_premium
from .generator import generate_workout_for_day, generate_full_weekly_schedule


@login_required
def generate_workout(request):
    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 30,
            'height': 170.0,
            'weight': 70.0,
            'goal': 'fitness',
            'experience': 'beginner'
        }
    )

    workout = generate_workout_for_day(profile=profile)

    return render(request, 'workouts/workout_plan.html', {
        'profile': profile,
        'workout': workout,
    })


@login_required
def weekly_schedule(request):
    if not is_premium(request.user):
        return HttpResponseForbidden(
            "Upgrade to Premium to access this feature"
        )

    profile, _ = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 30,
            'height': 170.0,
            'weight': 70.0,
            'goal': 'fitness',
            'experience': 'beginner'
        }
    )

    schedule = generate_full_weekly_schedule(profile=profile)

    return render(request, 'workouts/weekly_schedule.html', {
        'profile': profile,
        'schedule': schedule,
    })
