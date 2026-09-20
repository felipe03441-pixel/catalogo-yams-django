import os
import django
import pandas as pd

# 1. Conectar este script externo con el entorno de tu proyecto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yams_project.settings')
django.setup()

# 2. Importar los modelos después de iniciar Django
from catalogo.models import Categoria, Producto

print("Creando categorías base...")
categorias_lista = ['Anime', 'Papelería', 'Variedades', 'Tecnología', 'Series y Películas', 'Kpop']

for nombre_cat in categorias_lista:
    Categoria.objects.get_or_create(nombre=nombre_cat)

print("Leyendo el catálogo limpio de Excel...")
df = pd.read_excel('inventario_catalogo.xlsx')

# Solución al error 'nan': Rellenar las celdas vacías de precio y stock con el número 0
df['precio'] = df['precio'].fillna(0)
df['stock'] = df['stock'].fillna(0)

categoria_por_defecto = Categoria.objects.get(nombre='Variedades')

print("Importando productos a la base de datos...")
productos_creados = 0

for index, fila in df.iterrows():
    # Nos aseguramos de convertir los valores a enteros por si Pandas los dejó con decimales
    precio_limpio = int(fila['precio'])
    stock_limpio = int(fila['stock'])
    
    producto, creado = Producto.objects.get_or_create(
        nombre=fila['nombre'],
        defaults={
            'categoria': categoria_por_defecto,
            'precio': precio_limpio,
            'stock': stock_limpio
        }
    )
    if creado:
        productos_creados += 1

print(f"¡Proceso finalizado! Se importaron {productos_creados} productos a tu base de datos.")