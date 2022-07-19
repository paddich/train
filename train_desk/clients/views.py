from django.shortcuts import render

def clients_home(request):
    data = {
        'title': 'Клиенты',
        'clients_name': ['Петров', 'Сидоров', 'Козлов']
    }
    return render(request, 'clients/clients_home.html', data)

def clients_set(request):
    data = {
        'title': 'Настройки клиентов',
        'options': ['Сортировать по', 'Удалять не активных', 'Выделять цветом']
    }
    return render(request, 'clients/settings.html', data)

def client_add(request):
    data = {
        'title': 'Добавление клиента'
    }
    return render(request, 'clients/client_add.html', data)
