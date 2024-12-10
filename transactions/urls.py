# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    # Transaction URLs
    path('', views.transaction_list, name='transaction_list'),
    path('add/', views.transaction_add, name='transaction_add'),
    path('<int:id>/', views.transaction_detail, name='transaction_detail'),
    path('<int:id>/edit/', views.transaction_edit, name='transaction_edit'),
    path('<int:id>/delete/', views.transaction_delete, name='transaction_delete'),
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<int:id>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:id>/delete/', views.category_delete, name='category_delete'),
]
