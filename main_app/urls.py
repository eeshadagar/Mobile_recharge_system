from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home', views.home_page, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('details', views.details, name='details'),
    path('edit/<id>', views.edit, name='edit'),
    path('edit/details/<id>', views.afteredit, name='details'),
    path('delete/<id>', views.delete, name='delete'),
    path('deletee/<id>', views.deletee, name='deletee'),
    path('editt/<id>', views.editt, name='editt'),
    path('editt/details/<id>', views.aftereditt, name='details'),
]