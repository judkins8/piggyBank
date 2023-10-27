from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AllowanceEntryForm, PurchaseForm
# Create your views here.

def piggyBankPagesView(request) :
    return render(request, 'base.html')


def parent_dashboard(request):
    if request.method == 'POST':
        form = AllowanceEntryForm(request.POST)
        if form.is_valid():
            allowance_entry = form.save(commit=False)
            allowance_entry.child = request.user.child
            allowance_entry.save()
            return redirect('parent_dashboard')
    else:
        form = AllowanceEntryForm()

    return render(request, 'parent_dashboard.html', {'form': form})
