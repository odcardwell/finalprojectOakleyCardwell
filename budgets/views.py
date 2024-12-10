# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Budget
from .forms import BudgetForm

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    context = {
        'budgets': budgets,
    }
    return render(request, 'budgets/budget_list.html', context)

@login_required
def budget_add(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budgets:budget_list')
    else:
        form = BudgetForm()
    context = {
        'form': form,
        'action': 'Add',
    }
    return render(request, 'budgets/budget_form.html', context)

@login_required
def budget_detail(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    context = {
        'budget': budget,
    }
    return render(request, 'budgets/budget_detail.html', context)

@login_required
def budget_edit(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budgets:budget_list')
    else:
        form = BudgetForm(instance=budget)
    context = {
        'form': form,
        'action': 'Edit',
    }
    return render(request, 'budgets/budget_form.html', context)

@login_required
def budget_delete(request, id):
    budget = get_object_or_404(Budget, id=id, user=request.user)
    if request.method == 'POST':
        budget.delete()
        return redirect('budgets:budget_list')
    return render(request, 'budgets/budget_confirm_delete.html', {'budget': budget})

