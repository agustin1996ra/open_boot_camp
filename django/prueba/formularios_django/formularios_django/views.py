from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm({'name': 'Agus', 'url': 'https://www.youtube.com', 'comment': 'Comentario por defecto'})
    return render(request, 'form.html', {"comment_form": comment_form})

def goal(request):
    if request.method != "POST":
        return HttpResponse('Método no soportado por esta ruta')

    return HttpResponse(request.POST["name"])

def widget(request):
    if request.method == 'GET':
        form = ContactForm()
        return render(request, 'widget.html', {'form': form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aquí irán todas las acciones a realizar cuando los datos son correctos
            return HttpResponse("Válido")
        else:
            # Aquí comunicamos al usuario que los datos no son válidos
            return render(request, 'widget.html', {'form': form})
        