from django.urls import path
from . import views

urlpatterns = [
    path('', views.train_home, name='train_home'),
]