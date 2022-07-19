from django.urls import path
from . import views

urlpatterns = {
    path('', views.index, name='clients_home'),
    path('settings', views.settings, name='clients_set'),
    path('client', views.client, name='client_add'),
}