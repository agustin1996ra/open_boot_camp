from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse


def queries(request):
    # Obtener todos los elementos del modelo Author
    authors = Author.objects.all()

    # Obtener datos filtrados por condición
    filtered = Author.objects.filter(email='kreed@example.com')

    # Obtener un único objeto (filtrado)
    author = Author.objects.get(id=1)

    # Obtener los 10 primeros elementos
    limits = Author.objects.all()[:10]

    # Obtener los elementos del 5 al 10
    offsets = Author.objects.all()[5:10]

    # Obtener todos los elementos ordenados
    orders = Author.objects.all().order_by('email')

    # Obtener todos los elementos que su id sea menor o igual a 15
    filtereds = Author.objects.filter(id__lte=15)
    
    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'orders': orders, 'filtereds': filtereds})


def update(request):
    author = Author.objects.get(id=1)
    author.name = "Agustin"
    author.email = 'agus@demo.com'
    author.save()
    return HttpResponse("El elemento a sido actualizado")
