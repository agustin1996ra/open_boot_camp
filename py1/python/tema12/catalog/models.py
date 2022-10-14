from django.db import models


class Genere(models.Model):  # De la que heredaremos las propiedades de Model().
    name = models.CharField(max_length=64, help_text='Pon el nombre del genero')

    def __str__(self):  # Esto nos da una representación informal de una objeto
        return self.name
