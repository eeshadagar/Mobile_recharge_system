from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('paymentpre', views.payment_pre, name='paymentpre'),
    path('paymentpost', views.payment_post, name='paymentpost'),
]