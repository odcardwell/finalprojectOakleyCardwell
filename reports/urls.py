# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.monthly_summary, name='monthly_summary'),  # Root of the reports app
    path('monthly-summary/', views.monthly_summary, name='monthly_summary'),
]


