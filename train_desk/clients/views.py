from django.shortcuts import render
from django.http import HttpResponseNotFound

def clients_index(request):
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

# list_of_pages = {
#     'settings': 'clients/settings.html',
#     'add': 'clients/client_add.html'
# }
#
# def get_client_operation(request, client_operations: str):
#     description = list_of_pages.get(client_operations, None)
#     if description:
#         return render(request, description)
#     else:
#         return HttpResponseNotFound(f'Страница {client_operations} отсутствует')



# def get_new_client(request, client_name):
#     if client_name == Egor:
#         return render(request, )