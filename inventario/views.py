# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core import serializers
import json
from .models import Codigo, Articulo
from django.views.decorators.csrf import csrf_exempt

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
    return HttpResponse(data, content_type='application/json', status=200)

@csrf_exempt
def codigo_index(request):

    if request.method == 'POST':
        #Crear registro
        """Postman
        Codigo.objects.create(
            codigo = request.POST.get('codigo'),
            significado = request.POST.get('significado')
        )
        """
        #fetch
        data = json.loads(request.body)

        Codigo.objects.create(
            codigo =  data['codigo'],
            significado =  data['significado']
        )
        return HttpResponse(status=200)

    elif request.method == 'GET':
        #Obtener registros
        consulta = Codigo.objects.all()
        data = {}

        acum = 0
        for objeto in consulta:
            data[acum] = {
                'id' : objeto.pk,
                'codigo' : objeto.codigo,
                'significado' : objeto.significado
            }
            acum += 1

        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json', status=200)



def articulo(request, articulo_id):
    return HttpResponse(articulo_id)

"""Obtener registros peticion fetch
var url = "http://localhost:8000/api/inventario/codigo/",
		params = {
			method: "GET"
		};

	fetch( url, params)
	    .then( r => r.json())
    	.then( data => console.info( data ) )
	    .catch( e => alert("Los datos no han sido envidos")
	);
"""
"""Crear un nuevo codigo peticion fetch
var url = "http://localhost:8000/api/inventario/codigo/",
	params = {
		method: "POST",
		headers: {
        	'Accept': 'application/json',
			'Content-Type': 'application/json'
      	},
		body: JSON.stringify({
			codigo : 'BMK-A3-XXXX',
            significado: 'HERRAMIENTAS'
		})
	};

	fetch( url, params)
	    .then( () => alert("Los datos han sido envidos") )
	    .catch( e => alert("Los datos no han sido envidos")
);
"""
