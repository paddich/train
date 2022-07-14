from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', 'etc']
    }
    return render(request, 'clients/clients_home.html', data)

def settings(request):
    return render(request, 'clients/settings.html')
