from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('consulta/', views.consulta, name='consulta')
]
