from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', 'etc']
    }
    return render(request, 'clients/clients_home.html', data)

def settings(request):
    return HttpResponse('<h2>Test text settings</h2> ')
