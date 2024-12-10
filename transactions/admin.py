# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.contrib import admin

from django.contrib import admin
from .models import Transaction, Category

admin.site.register(Transaction)
admin.site.register(Category)

