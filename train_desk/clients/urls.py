from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients_index, name='clients_home'),
    path('settings', views.clients_set, name='clients_set'),
    path('add', views.client_add, name='client_add'),
    # path('<client_operations>', views.get_client_operation),
    # path('<client_name>', views.get_new_client, name='get_a_new_client'),
]