from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'amount', 'description', 'transaction_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class SavingsGoalForm(forms.Form):
    savings_goal = forms.DecimalField(max_digits=10, decimal_places=2, label='Savings Goal')
