from django.shortcuts import render, redirect
from .models import Transaction, SavingsGoal  # Make sure to import SavingsGoal model
from .forms import TransactionForm, SavingsGoalForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

@login_required
def index(request):
    transaction_form = TransactionForm()
    savings_goal_form = SavingsGoalForm()

    # Handle transactions
    if 'amount' in request.POST:  # Check if transaction is being posted
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('index')

    # Handle savings goal
    elif 'goal_amount' in request.POST:  # Check if savings goal is being posted
        savings_goal_form = SavingsGoalForm(request.POST)
        if savings_goal_form.is_valid():
            # Get or create a savings goal instance
            savings_goal, created = SavingsGoal.objects.get_or_create(
                user=request.user,
                defaults={'goal_amount': savings_goal_form.cleaned_data['goal_amount']}
            )
            if not created:
                # If a SavingsGoal already exists, update it
                savings_goal.goal_amount = savings_goal_form.cleaned_data['goal_amount']
                savings_goal.save()
            return redirect('index')

    transactions = Transaction.objects.filter(user=request.user)
    total_balance = sum(transaction.amount for transaction in transactions)
    
    # Fetch the user's savings goal from the database, or default to zero if not set
    try:
        savings_goal_instance = SavingsGoal.objects.get(user=request.user)
        savings_goal = savings_goal_instance.goal_amount
    except SavingsGoal.DoesNotExist:
        savings_goal = 0

    context = {
        'transaction_form': transaction_form,
        'transactions': transactions,
        'total_balance': total_balance,
        'savings_goal': savings_goal,  # This should come from the database now
        'savings_goal_form': savings_goal_form,
    }
    return render(request, 'piggyBankPages/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Authenticate the user manually
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # Log the user in
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            # Redirect to 'index' or another desired page after successful registration
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def transaction_view(request):
    if request.method == 'POST':
        transaction_form = TransactionForm(request.POST)
        if transaction_form.is_valid():
            transaction = transaction_form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('index')  # Make sure to redirect to the correct view
    else:
        transaction_form = TransactionForm()
    return render(request, 'some_template.html', {'form': TransactionForm})  # Specify the correct template
