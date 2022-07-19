from django.shortcuts import render

def main_home(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', 'etc']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')