# -*- coding: utf-8 -*-
from django.http import HttpResponse
import json
from .models import Codigo, Articulo
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse('Bienvenido al api de BMKeros')


@csrf_exempt
def codigo(request, codigo_id):
    # Funcion para obtener un registro, actualizar un registro y eliminar alguno en especifico.
    if request.method == 'GET':
        consulta = Codigo.objects.filter(id=codigo_id)
        data = {}
        for objeto in consulta:
            data['id'] = objeto.pk
            data['codigo'] = objeto.codigo
            data['significado'] = objeto.significado

        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json', status=200)

    if request.method == 'POST':

        data = json.loads(request.body)
        if data['accion'] == 'actualizar':
            consulta = Codigo.objects.filter(id=codigo_id).get()
            consulta.codigo = data['codigo']
            consulta.significado = data['significado']
            consulta.save()
            return HttpResponse('Registro actualizado con exito', status=200)

        elif data['accion'] == 'eliminar':
            Codigo.objects.filter(id=codigo_id).delete()
            # consulta.detele()
            return HttpResponse('Registro eliminado con exito', status=200)



@csrf_exempt
def codigo_index(request):
    # Funcion para obtener todos los registros y ademas crear uno.
    if request.method == 'POST':

        data = json.loads(request.body)

        # Crear registro
        Codigo.objects.create(
            codigo=data['codigo'],
            significado=data['significado']
        )
        return HttpResponse('Registro creado con exito', status=200)

    elif request.method == 'GET':
        # Obtener todos los registros
        consulta = Codigo.objects.all()
        data = {}

        acum = 0
        for objeto in consulta:
            data[acum] = {
                'id': objeto.pk,
                'codigo': objeto.codigo,
                'significado': objeto.significado
            }
            acum += 1

        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json', status=200)


def articulo(request, articulo_id):
    return HttpResponse(articulo_id)


# Peticiones fecth modelo codigo

"""
var url = "http://localhost:8000/api/inventario/codigo/5",
		params = {
			method: "GET"
		};

	fetch( url, params)
	    .then( r => r.json())
    	.then( data => console.info( data ) )
	    .catch( e => alert("Los datos no han sido envidos")
	);
"""

"""Obtener todos los registros peticion fetch
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

"""Actializar un registro

"""


"""Eliminar un registro
var url = "http://localhost:8000/api/inventario/codigo/12",
	params = {
		method: "POST",
		headers: {
        	'Accept': 'application/json',
			'Content-Type': 'application/json'
      	},
		body: JSON.stringify({
			
            accion: 'eliminar'
		})
	};

	fetch( url, params)
	    .then( () => alert("Los datos han sido envidos") )
	    .catch( e => alert("Los datos no han sido envidos")
);
"""
