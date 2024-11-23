from django.db import models

from django.db import models
from django.contrib.auth.models import User
from transactions.models import Category

class Budget(models.Model):
    """Model to represent user budgets."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='budgets')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Budget of ${self.amount} for {self.category.name}"

