# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core import serializers
import json
from .models import Codigo, Articulo

def index(request):
    return HttpResponse('Bienvenido al api de BMKeros')

def codigo(request, codigo_id):
    consulta = Codigo.objects.filter(id=codigo_id)
    data = {}
    for objeto in consulta:
        data['id'] = objeto.pk
        data['codigo'] = objeto.codigo
        data['significado'] = objeto.significado

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def codigo_index(request):
    consulta = Codigo.objects.all()
    data = {}

    acum = 0
    for objeto in consulta:
        data[acum] = {
            'id' : objeto.pk,
            'codigo' : objeto.codigo,
            'significado' : objeto.significado
        }
        acum = + 1

    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def articulo(request, articulo_id):
    return HttpResponse(articulo_id)
