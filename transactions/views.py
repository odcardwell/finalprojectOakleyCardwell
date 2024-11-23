from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def transaction_list(request):
    # Placeholder for transaction list
    return render(request, 'transactions/transaction_list.html')

@login_required
def transaction_add(request):
    # Placeholder for adding a transaction
    return render(request, 'transactions/transaction_add.html')

@login_required
def transaction_detail(request, id):
    # Placeholder for transaction detail
    return render(request, 'transactions/transaction_detail.html', {'id': id})

@login_required
def transaction_edit(request, id):
    # Placeholder for editing a transaction
    return render(request, 'transactions/transaction_edit.html', {'id': id})

@login_required
def transaction_delete(request, id):
    # Placeholder for deleting a transaction
    return redirect('transactions:transaction_list')

