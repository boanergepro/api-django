# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from .models import Codigo, Articulo

def index(request):
    return HttpResponse('Bienvenido al api de BMKeros')

def codigo(request, codigo_id):
    consulta = Codigo.objects.get(id=codigo_id)
    return HttpResponse(consulta)

def articulo(request, articulo_id):
    return HttpResponse(articulo_id)
