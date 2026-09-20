from django.shortcuts import render
from django.core.paginator import Paginator # <-- Nueva herramienta importada
from .models import Producto, Categoria

def catalogo_view(request):
    categoria_id = request.GET.get('categoria')
    query = request.GET.get('q') 
    
    # Iniciamos con todos los productos disponibles
    productos = Producto.objects.filter(stock__gt=0)
    
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
        
    if query:
        productos = productos.filter(nombre__icontains=query)
        
    categorias = Categoria.objects.all()
    
    # --- NUEVA LÓGICA DE PAGINACIÓN ---
    # Dividimos los productos para mostrar 20 por página
    paginator = Paginator(productos, 20)
    
    # Capturamos el número de página actual desde la dirección web (ej. ?page=2)
    page_number = request.GET.get('page')
    
    # Obtenemos únicamente los productos correspondientes a esa página
    productos_paginados = paginator.get_page(page_number)
    
    return render(request, 'catalogo/index.html', {
        'productos': productos_paginados, # Ahora enviamos la variable paginada
        'categorias': categorias,
        'query': query,
        'categoria_actual': categoria_id
    })