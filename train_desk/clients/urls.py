from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_home, name='clients_home'),
    path('settings', views.clients_set, name='clients_set'),
    path('add', views.client_add, name='client_add')
]