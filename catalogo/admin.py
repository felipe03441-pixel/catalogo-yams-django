from django.contrib import admin
from django import forms
from .models import Producto, ImagenProducto

# 1. Creamos nuestro propio componente visual con permiso para múltiples archivos
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# 2. Usamos nuestro nuevo componente en el formulario
class ProductoAdminForm(forms.ModelForm):
    fotos_multiples = forms.FileField(
        # Aquí llamamos a nuestra nueva clase especial MultipleFileInput
        widget=MultipleFileInput(attrs={'multiple': True}),
        label="Subir múltiples fotos a la galería (Selecciona varias a la vez)",
        required=False
    )

    class Meta:
        model = Producto
        fields = '__all__'

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto
    extra = 0 

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoAdminForm
    inlines = [ImagenProductoInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        fotos = request.FILES.getlist('fotos_multiples')
        for foto in fotos:
            ImagenProducto.objects.create(producto=obj, imagen=foto)

admin.site.register(Producto, ProductoAdmin)