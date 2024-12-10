# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Extended user profile model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add extra fields here, e.g., preferred currency
    currency = models.CharField(max_length=10, default='USD')

    def __str__(self):
        return self.user.username

