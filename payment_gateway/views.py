from django.shortcuts import render, redirect
from .forms import PaymentForm_pre, PaymentForm_post

# Create your views here.

def payment_pre(request):
    if request.method == "POST":
        form = PaymentForm_pre(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.name = request.user
            record.save()
            return redirect("main_app:details")
    else:
        form = PaymentForm_pre()
    
    return render(request, 'payment.html', {'form':form})

def payment_post(request):
    if request.method == "POST":
        form = PaymentForm_post(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.name = request.user
            record.save()
            return redirect("main_app:details")
    else:
        form = PaymentForm_post()
    
    return render(request, 'payment.html', {'form':form})