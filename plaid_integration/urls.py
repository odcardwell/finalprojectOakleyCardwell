# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.urls import path
from . import views

app_name = 'plaid'  # Ensure this line is present and correct

urlpatterns = [
    path('link_account/', views.link_account, name='link_account'),
    path('get_link_token/', views.get_link_token, name='get_link_token'),
    path('exchange_public_token/', views.exchange_public_token, name='exchange_public_token'),
    path('fetch_transactions/', views.fetch_transactions, name='fetch_transactions'),
]

