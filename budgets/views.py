from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# budgets/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Budget
from .forms import BudgetForm

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'budgets/budget_list.html', {'budgets': budgets})

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
    return render(request, 'budgets/budget_form.html', {'form': form, 'action': 'Add'})

@login_required
def budget_detail(request, id):
    budget = get_object_or_404(Budget, id=id, user=request.user)
    return render(request, 'budgets/budget_detail.html', {'budget': budget})

@login_required
def budget_edit(request, id):
    budget = get_object_or_404(Budget, id=id, user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budgets:budget_list')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'budgets/budget_form.html', {'form': form, 'action': 'Edit'})

@login_required
def budget_delete(request, id):
    budget = get_object_or_404(Budget, id=id, user=request.user)
    if request.method == 'POST':
        budget.delete()
        return redirect('budgets:budget_list')
    return render(request, 'budgets/budget_confirm_delete.html', {'budget': budget})


