# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')
