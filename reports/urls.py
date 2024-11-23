from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.report_dashboard, name='report_dashboard'),
    path('export/', views.report_export, name='report_export'),
]
