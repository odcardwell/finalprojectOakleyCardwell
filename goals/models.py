from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    """Model to represent financial goals."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    name = models.CharField(max_length=100)
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    deadline = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

