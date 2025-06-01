from django.shortcuts import render
from .models import postrecharge
from .forms import PostRechargeForm
from django.shortcuts import redirect
import requests
from bs4 import BeautifulSoup
# Create your views here.

def postrechargee(request):
    if request.method == "POST":
        form = PostRechargeForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect("postpaid:plans")
    else:
        form = PostRechargeForm()
    return render(request, 'post_recharge.html', {'form':form})

def plans(request):
    info = postrecharge.objects.values_list('operator','region')
    i = len(info)-1
    infoo = info[i]
    operatorr = infoo[0]
    region = infoo[1]
    url = "https://www.plansinfo.com/mobile/"+operatorr+"/"+region
    page = requests.get(url)
    Soup = BeautifulSoup(page.content, 'html.parser')
    rs = Soup.find_all(class_='amount')
    des = Soup.find_all(class_='benefit')
    rss = [items.get_text() for items in rs]
    dess = [items.get_text() for items in des]
    plans = {'rs':rss,'des':dess}
    return render(request, 'plans.html', {'plans':plans})
