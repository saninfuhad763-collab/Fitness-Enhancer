from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from users.models import UserProfile
from .models import WorkoutPlan, WeeklyWorkout

from users.utils import is_premium
from django.http import HttpResponseForbidden


@login_required
def generate_workout(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 30,
            'height': 170.0,
            'weight': 70.0,
            'goal': 'fitness',
            'experience': 'beginner'
        }
    )

    plan = WorkoutPlan.objects.filter(
        goal=profile.goal,
        level=profile.experience
    ).first()

    return render(request, 'workouts/workout_plan.html', {
        'plan': plan
    })


@login_required
def weekly_schedule(request):

    if not is_premium(request.user):
        return HttpResponseForbidden(
            "Upgrade to Premium to access this feature"
        )

    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 30,
            'height': 170.0,
            'weight': 70.0,
            'goal': 'fitness',
            'experience': 'beginner'
        }
    )

    # Get suitable workout plan
    plan = WorkoutPlan.objects.filter(
        goal=profile.goal,
        level=profile.experience
    ).first()

    days = ['mon', 'tue', 'wed', 'fri', 'sat']  # rest: thu, sun

    # Reset old schedule
    WeeklyWorkout.objects.filter(user=request.user).delete()

    for day in days:
        WeeklyWorkout.objects.create(
            user=request.user,
            day=day,
            workout_plan=plan
        )

    schedule = WeeklyWorkout.objects.filter(user=request.user)

    return render(request, 'workouts/weekly_schedule.html', {
        'schedule': schedule
    })
