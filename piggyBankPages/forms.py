# piggybank_app/forms.py

from django import forms
from .models import AllowanceEntry, Purchase

class AllowanceEntryForm(forms.ModelForm):
    class Meta:
        model = AllowanceEntry
        fields = ['date', 'amount', 'chore_description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['date', 'amount', 'description']
