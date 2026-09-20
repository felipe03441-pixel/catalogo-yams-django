# catalogo/models.py

from django.db import models

class Categoria(models.Model):
    # Aquí definiremos anime, papelería, tecnología, etc.
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    # Vinculamos el producto a una categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField(help_text="Precio en números enteros")
    stock = models.IntegerField(default=0)
    # Espacio para una sola imagen
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre