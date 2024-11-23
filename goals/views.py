from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# goals/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Goal
from .forms import GoalForm

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals/goal_list.html', {'goals': goals})

@login_required
def goal_add(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('goals:goal_list')
    else:
        form = GoalForm()
    return render(request, 'goals/goal_form.html', {'form': form, 'action': 'Add'})

@login_required
def goal_detail(request, id):
    goal = get_object_or_404(Goal, id=id, user=request.user)
    return render(request, 'goals/goal_detail.html', {'goal': goal})

@login_required
def goal_edit(request, id):
    goal = get_object_or_404(Goal, id=id, user=request.user)
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('goals:goal_list')
    else:
        form = GoalForm(instance=goal)
    return render(request, 'goals/goal_form.html', {'form': form, 'action': 'Edit'})

@login_required
def goal_delete(request, id):
    goal = get_object_or_404(Goal, id=id, user=request.user)
    if request.method == 'POST':
        goal.delete()
        return redirect('goals:goal_list')
    return render(request, 'goals/goal_confirm_delete.html', {'goal': goal})



