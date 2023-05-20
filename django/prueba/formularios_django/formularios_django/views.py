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
    form = ContactForm()
    return render(request, 'widget.html', {'form': form})
