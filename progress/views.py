

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WeightProgress
from .forms import WeightProgressForm
from django.http import HttpResponseForbidden
from users.utils import is_premium

@login_required
def progress_view(request):
    if request.method == 'POST':
        form = WeightProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.save()
            return redirect('progress')
    else:
        form = WeightProgressForm()

    progress_data = WeightProgress.objects.filter(
        user=request.user
    ).order_by('date')

    dates = [p.date.strftime('%Y-%m-%d') for p in progress_data]
    weights = [p.weight for p in progress_data]

    context = {
        'form': form,
        'dates': dates,
        'weights': weights,
        'progress_data': progress_data,
    }

    return render(request, 'progress/progress.html', context)


@login_required
def progress_charts(request):

    # 🔐 PREMIUM CHECK
    if not is_premium(request.user):
        return HttpResponseForbidden(
            "Upgrade to Premium to view progress charts"
        )

    return render(request, 'progress/progress_charts.html')