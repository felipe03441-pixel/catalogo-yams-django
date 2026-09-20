# catalogo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Cuando la ruta esté vacía (página principal), ejecuta la vista del catálogo
    path('', views.catalogo_view, name='catalogo_view'),
]