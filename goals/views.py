from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def goal_list(request):
    # Placeholder for goal list
    return render(request, 'goals/goal_list.html')

@login_required
def goal_add(request):
    # Placeholder for adding a goal
    return render(request, 'goals/goal_add.html')

@login_required
def goal_detail(request, id):
    # Placeholder for goal detail
    return render(request, 'goals/goal_detail.html', {'id': id})

@login_required
def goal_edit(request, id):
    # Placeholder for editing a goal
    return render(request, 'goals/goal_edit.html', {'id': id})

@login_required
def goal_delete(request, id):
    # Placeholder for deleting a goal
    return redirect('goals:goal_list')


