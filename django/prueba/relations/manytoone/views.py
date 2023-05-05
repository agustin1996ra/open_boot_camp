from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

def create(request):
    rep = Reporter(first_name='Agus', last_name='Rodriguez', email='agusrodriguez@demo.net')
    rep.save()

    art1 = Article(headline='El que sea', pub_date=date(2022,5,5), reporter=rep)
    art1.save()
    art2 = Article(headline='Hola que tal', pub_date=date(2022,6,5), reporter=rep)
    art2.save()
    art3 = Article(headline='Como estas?', pub_date=date(2022,7,5), reporter=rep)
    art3.save()

    # query = art1.reporter.first_name
    query = rep.article_set.all()
    # query = rep.article_set.filter(id=2)
    # query = rep.article_set.count()

    return HttpResponse(query)
