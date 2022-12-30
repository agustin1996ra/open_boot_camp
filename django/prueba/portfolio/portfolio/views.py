from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def galeria(request):
    return render(request, 'galeria.html', {})