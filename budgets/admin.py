# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.contrib import admin
from .models import Budget

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'start_date', 'end_date')
    list_filter = ('category', 'start_date', 'end_date')

admin.site.register(Budget, BudgetAdmin)

