# budgets/urls.py
from django.urls import path
from . import views

app_name = 'budgets'

urlpatterns = [
    path('', views.budget_list, name='budget_list'),
    path('add/', views.budget_add, name='budget_add'),
    path('<int:id>/', views.budget_detail, name='budget_detail'),
    path('<int:id>/edit/', views.budget_edit, name='budget_edit'),
    path('<int:id>/delete/', views.budget_delete, name='budget_delete'),
]
