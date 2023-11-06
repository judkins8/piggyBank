from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm, SavingsGoalForm

def index(request):
    # Handle savings goal
    if request.method == 'POST' and 'savings_goal' in request.POST:
        savings_goal_form = SavingsGoalForm(request.POST)
        if savings_goal_form.is_valid():
            request.session['savings_goal'] = str(savings_goal_form.cleaned_data['savings_goal'])
            return redirect('index')
    else:
        savings_goal_form = SavingsGoalForm(initial={'savings_goal': request.session.get('savings_goal', '0')})

    # Handle transactions
    if request.method == 'POST' and 'amount' in request.POST:
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction_form.save()
            return redirect('index')
    else:
        transaction_form = TransactionForm()

    transactions = Transaction.objects.all()
    
    # Convert the Decimal to a string to preserve precision
    total_balance = sum(transaction.amount for transaction in transactions)
    total_balance = float(total_balance)  # Convert total_balance to float
    savings_goal = float(request.session.get('savings_goal', 0))

    context = {
        'transaction_form': transaction_form,
        'savings_goal_form': savings_goal_form,
        'transactions': transactions,
        'total_balance': total_balance,  # Now a float, not a Decimal
        'savings_goal': savings_goal,
    }
    return render(request, 'piggyBankPages/index.html', context)
