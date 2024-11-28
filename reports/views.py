from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from django.db.models.functions import TruncMonth, Abs
from transactions.models import Transaction
from budgets.models import Budget
import json
from collections import defaultdict

@login_required
def monthly_summary(request):
    # Existing code to aggregate income and expenses per month
    transactions = Transaction.objects.filter(user=request.user)
    income_data = (
        transactions.filter(transaction_type='income')
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )
    expense_data = (
        transactions.filter(transaction_type='expense')
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    # Prepare data for the chart
    monthly_data = defaultdict(lambda: {'income': 0, 'expense': 0})

    for entry in income_data:
        month_str = entry['month'].strftime('%Y-%m')
        monthly_data[month_str]['income'] = float(entry['total'])

    for entry in expense_data:
        month_str = entry['month'].strftime('%Y-%m')
        monthly_data[month_str]['expense'] = float(entry['total'])

    months = sorted(monthly_data.keys())
    income_totals = [monthly_data[month]['income'] for month in months]
    expense_totals = [monthly_data[month]['expense'] for month in months]

    # Prepare budget performance data
    budgets = Budget.objects.filter(user=request.user)
    budget_data = []

    for budget in budgets:
        # Calculate total expenses for the budget category and period
        total_expenses = Transaction.objects.filter(
            user=request.user,
            category=budget.category,
            transaction_type='expense',
            date__gte=budget.start_date,
            date__lte=budget.end_date
        ).aggregate(total=Sum(Abs(F('amount'))))['total'] or 0

        # Calculate the percentage used
        if budget.amount:
            percentage_used = (total_expenses / budget.amount) * 100
        else:
            percentage_used = 100 if total_expenses > 0 else 0

        # Determine if over or under budget
        status = 'Under Budget' if total_expenses <= budget.amount else 'Over Budget'

        # Calculate remaining amount
        remaining_amount = budget.amount - total_expenses

        budget_data.append({
            'budget': budget,
            'total_expenses': total_expenses,
            'remaining_amount': remaining_amount,
            'percentage_used': percentage_used,
            'status': status,
        })

    # Prepare context data
    context = {
        'months': json.dumps(months),
        'income_totals': json.dumps(income_totals),
        'expense_totals': json.dumps(expense_totals),
        'budget_data': budget_data,
    }
    return render(request, 'reports/monthly_summary.html', context)




