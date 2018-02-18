from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<articulo_id>[0-9]+)/$', views.articulo, name='articulo'),
    #/api/inventario/1/codigo
    url(r'^(?P<codigo_id>[0-9]+)/codigo/$', views.codigo, name='codigo'),
]
