# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.db import models
from django.contrib.auth.models import User
from transactions.models import Category
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Budget(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('biweekly', 'Bi-Weekly'),
        ('monthly', 'Monthly'),
        ('annually', 'Annually'),
        ('custom', 'Custom Range'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES, default='monthly')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def current_period_dates(self):
        today = timezone.now().date()
        if self.period == 'daily':
            start = today
            end = today
        elif self.period == 'weekly':
            start = today - relativedelta(days=today.weekday())  # Start of the week (Monday)
            end = start + relativedelta(days=6)
        elif self.period == 'biweekly':
            # Start from the first Monday of the year
            first_monday = today.replace(month=1, day=1)
            if first_monday.weekday() != 0:
                first_monday += relativedelta(days=(7 - first_monday.weekday()))
            delta_days = (today - first_monday).days
            periods_passed = delta_days // 14
            start = first_monday + relativedelta(days=periods_passed * 14)
            end = start + relativedelta(days=13)
        elif self.period == 'monthly':
            start = today.replace(day=1)
            end = (start + relativedelta(months=1)) - relativedelta(days=1)
        elif self.period == 'annually':
            start = today.replace(month=1, day=1)
            end = today.replace(month=12, day=31)
        elif self.period == 'custom':
            start = self.start_date
            end = self.end_date
        else:
            start = None
            end = None
        return start, end


