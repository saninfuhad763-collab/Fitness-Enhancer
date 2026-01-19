from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import CustomUserRegistrationForm
from .models import UserProfile, Subscription


@login_required
def dashboard(request):
    profile = UserProfile.objects.get(user=request.user)

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

            # Create user profile
            UserProfile.objects.create(
                user=user,
                age=form.cleaned_data['age'],
                height=form.cleaned_data['height'],
                weight=form.cleaned_data['weight'],
                goal=form.cleaned_data['goal']
            )
            #assign free plan
            Subscription.objects.create(
                 user=user,
                 plan='free'
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

        