from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def report_dashboard(request):
    # Placeholder for report dashboard
    return render(request, 'reports/report_dashboard.html')

@login_required
def report_export(request):
    # Placeholder for exporting reports
    return render(request, 'reports/report_export.html')


