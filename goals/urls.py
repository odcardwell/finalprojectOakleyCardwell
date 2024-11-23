from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('add/', views.goal_add, name='goal_add'),
    path('<int:id>/', views.goal_detail, name='goal_detail'),
    path('<int:id>/edit/', views.goal_edit, name='goal_edit'),
    path('<int:id>/delete/', views.goal_delete, name='goal_delete'),
]
