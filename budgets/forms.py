# INF601 - Advanced Programming in Python
# Oakley Cardwell
# Final Project

from django import forms
from .models import Budget

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['category', 'amount', 'period', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is None or amount < 0:
            raise forms.ValidationError('Budget amount must be greater than or equal to zero.')
        return amount

    def clean(self):
        cleaned_data = super().clean()
        period = cleaned_data.get('period')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if period == 'custom':
            if not start_date or not end_date:
                raise forms.ValidationError('Start date and end date are required for custom periods.')
            if end_date < start_date:
                raise forms.ValidationError('End date must be after start date.')
        else:
            # Clear start_date and end_date for standard periods
            cleaned_data['start_date'] = None
            cleaned_data['end_date'] = None
        return cleaned_data

