# -*- coding: utf-8 -*-
from django.db import models

# Modelo codigos
class Codigo(models.Model):
    codigo = models.CharField(max_length=12)
    significado = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)

# Modelo articulo
class Articulo(models.Model):
    codigo = models.ForeignKey(Codigo)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    perdido = models.IntegerField()
    restante = models.IntegerField()
    def __str__(self):
        return str(self.id)
