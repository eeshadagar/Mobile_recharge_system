from django.urls import path
from . import views

app_name = 'postpaid'

urlpatterns = [
    path('/postrecharge', views.postrechargee, name='postrecharge'),
    path('/plans', views.plans, name='plans'),
]