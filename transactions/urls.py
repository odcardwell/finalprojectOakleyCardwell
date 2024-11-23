from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('add/', views.transaction_add, name='transaction_add'),
    path('<int:id>/', views.transaction_detail, name='transaction_detail'),
    path('<int:id>/edit/', views.transaction_edit, name='transaction_edit'),
    path('<int:id>/delete/', views.transaction_delete, name='transaction_delete'),
]
