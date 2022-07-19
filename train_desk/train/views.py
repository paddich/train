from django.shortcuts import render

def home(request):
    return render(request, 'train/train_home.html')
