from django.shortcuts import render

def index(request):
    data = {
        'title': 'Клиенты',
        'clients_name': ['Петров', 'Сидоров', 'Козлов']
    }
    return render(request, 'clients/clients_home.html', data)

def settings(request):
    return render(request, 'clients/settings.html')

def client(request):
    return render(request, 'clients/client_add.html')
