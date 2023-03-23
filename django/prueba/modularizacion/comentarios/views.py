from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    
    return HttpResponse("Ruta para probar la creación de modelos")
