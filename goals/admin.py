from django.contrib import admin

from django.contrib import admin
from .models import Goal

class GoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'target_amount', 'saved_amount', 'deadline')
    list_filter = ('deadline',)

admin.site.register(Goal, GoalAdmin)

