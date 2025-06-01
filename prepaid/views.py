from django.shortcuts import render, redirect
from .forms import RechargeForm

# Create your views here.

def recharge(request):
    if request.method == "POST":
        form = RechargeForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect("payment:paymentpre")
    else:
        form = RechargeForm()
    return render(request, 'Add_recharge.html', {'form':form})



