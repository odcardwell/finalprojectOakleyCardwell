# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
]
