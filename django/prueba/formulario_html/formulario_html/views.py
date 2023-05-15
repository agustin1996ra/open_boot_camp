from django.shortcuts import render
from django.http import HttpResponse

def get_form(request):
    return render(request, 'form.html', {})

def get_goal(request):
    if request.method != 'GET':
        return HttpResponse("El método POST no esta soportado para esta ruta")
    
    name = request.GET['name']
    return render(request, 'success.html', {'name': name})

def post_form(request):
    return render(request, 'postform.html', {})

def post_goal(request):
    if request.method != "POST":
        return HttpResponse("El método GET no esta soportado por esta ruta")
    
    info = request.POST['info']
    return render(request, 'postsuccess.html', {'info': info})

