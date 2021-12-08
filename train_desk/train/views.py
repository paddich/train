from django.http import HttpResponse
from django.shortcuts import render

def train_home(request):
    return HttpResponse('Крутые тренировки')