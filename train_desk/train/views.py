from django.http import HttpResponse
from django.shortcuts import render

def train_home(request):
    return render(request, 'train/train_home.html')