from django.urls import path
from . import views

app_name = 'prepaid'

urlpatterns = [
    path('/recharge', views.recharge, name='recharge'),
]