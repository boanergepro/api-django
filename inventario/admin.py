from django.contrib import admin

from .models import Codigo, Articulo

#Mostrar los modelos en la vista administrador

admin.site.register(Codigo)
admin.site.register(Articulo)
