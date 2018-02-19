from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<articulo_id>[0-9]+)/$', views.articulo, name='articulo'),
    #/api/inventario/codigo/1
    url(r'^codigo/(?P<codigo_id>[0-9]+)$', views.codigo, name='codigo'),
    #/api/inventario/codigo --> todos los registros
    url(r'codigo/', views.codigo_index, name='codigo'),
]
