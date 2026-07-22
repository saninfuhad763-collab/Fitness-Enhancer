from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from .forms import CustomUserRegistrationForm, UserProfileForm
from .models import UserProfile, Subscription


@login_required
def dashboard(request):
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'age': 30,
            'height': 170.0,
            'weight': 70.0,
            'goal': 'fitness'
        }
    )

    # BMI calculation
    height_m = profile.height / 100
    bmi = round(profile.weight / (height_m ** 2), 1)

    context = {
        'profile': profile,
        'bmi': bmi,
    }
    return render(request, 'dashboard/dashboard.html',context)


def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Create or update user profile (signal might have created it)
            UserProfile.objects.update_or_create(
                user=user,
                defaults={
                    'age': form.cleaned_data['age'],
                    'height': form.cleaned_data['height'],
                    'weight': form.cleaned_data['weight'],
                    'goal': form.cleaned_data['goal']
                }
            )
            # Assign free plan
            Subscription.objects.update_or_create(
                 user=user,
                 defaults={'plan': 'free'}
            )

            # Auto login after registration
            login(request, user)
            return redirect('dashboard')

    else:
        form = CustomUserRegistrationForm()

    return render(request, 'auth/register.html', {'form': form})

@login_required
def upgrade(request):
    return render(request, 'users/upgrade.html')


@login_required
def edit_profile(request):
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

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form, 'profile': profile})

        