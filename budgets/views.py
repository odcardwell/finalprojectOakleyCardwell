from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def budget_list(request):
    # Placeholder for budget list
    return render(request, 'budgets/budget_list.html')

@login_required
def budget_add(request):
    # Placeholder for adding a budget
    return render(request, 'budgets/budget_add.html')

@login_required
def budget_detail(request, id):
    # Placeholder for budget detail
    return render(request, 'budgets/budget_detail.html', {'id': id})

@login_required
def budget_edit(request, id):
    # Placeholder for editing a budget
    return render(request, 'budgets/budget_edit.html', {'id': id})

@login_required
def budget_delete(request, id):
    # Placeholder for deleting a budget
    return redirect('budgets:budget_list')

