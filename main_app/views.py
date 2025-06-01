from django.shortcuts import render
from .models import Detail
from postpaid.models import postrecharge
from payment_gateway.models import Payments_post
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def details(request):
    detail = Detail.objects.all
    postdeet = postrecharge.objects.all
    amount = Payments_post.objects.all
    details = {'detail':detail, 'postdeet':postdeet, 'amount':amount}
    return render(request, 'Recharge_details.html', details)

def edit(request, id):
    record = Detail.objects.get(id=id)
    template = loader.get_template('edit_record.html')
    context = {
        'record': record,
    }
    return HttpResponse(template.render(context, request))

def afteredit(request, id):
    number = request.POST['number']
    operator = request.POST['operator']
    new_record = Detail.objects.get(id=id)
    new_record.number = number
    new_record.operator = operator
    new_record.save()
    return redirect('main_app:details')

def delete(request, id):
    record = get_object_or_404(Detail, pk=id)
    record.delete()
    return redirect('main_app:details')

def editt(request, id):
    record = postrecharge.objects.get(id=id)
    template = loader.get_template('edit_record_post.html')
    context = {
        'record': record,
    }
    return HttpResponse(template.render(context, request))

def aftereditt(request, id):
    number = request.POST['number']
    operator = request.POST['operator']
    new_record = postrecharge.objects.get(id=id)
    new_record.number = number
    new_record.operator = operator
    new_record.save()
    return redirect('main_app:details')

def deletee(request, id):
    record = get_object_or_404(postrecharge, pk=id)
    record.delete()
    return redirect('main_app:details')