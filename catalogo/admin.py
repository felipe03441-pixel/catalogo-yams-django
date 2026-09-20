from django.contrib import admin
from .models import Categoria, Producto

# Habilitamos la edición de categorías
admin.site.register(Categoria)

# Habilitamos la edición de productos con una vista de tabla organizada
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista principal
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    # Filtro lateral para buscar rápidamente por categoría
    list_filter = ('categoria',)
    # Barra de búsqueda por nombre del producto
    search_fields = ('nombre',)