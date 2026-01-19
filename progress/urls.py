from django.urls import path
from .views import progress_view, progress_charts

urlpatterns = [
    path('', progress_view, name='progress'),
    path('charts/', progress_charts, name='progress_charts'),
]