from django import forms
from .models import Transaction, SavingsGoal
from django.forms import ModelForm


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'amount', 'description', 'transaction_type']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class SavingsGoalForm(ModelForm):
    class Meta:
        model = SavingsGoal
        fields = ['goal_amount']  # Or whichever fields you have