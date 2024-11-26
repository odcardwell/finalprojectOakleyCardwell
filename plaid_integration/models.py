# plaid_integration/models.py

from django.db import models
from django.contrib.auth.models import User

class PlaidAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.institution_name or 'Unknown Institution'}"

