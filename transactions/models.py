# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """Model to represent transaction categories."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    """Model to represent income and expense transactions."""
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='transactions')
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    description = models.CharField(max_length=255, blank=True)
    is_recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_transaction_type_display()} of ${self.amount} on {self.date}"

