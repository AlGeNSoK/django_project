from django.urls import path

from .views import SensorCreateView, SensorUpdateView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorCreateView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
