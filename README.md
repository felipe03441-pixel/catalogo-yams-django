# 🍠 Yams - Sistema Web de Gestión de Catálogos e Inventarios

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

## 📌 Descripción del Proyecto
**Yams** es una aplicación web y de escritorio diseñada para centralizar y optimizar la gestión de catálogos de productos y el control de inventarios. Este proyecto nace de la necesidad de digitalizar las operaciones comerciales, permitiendo a los vendedores administrar su stock, exportar reportes y compartir catálogos en línea de forma segura.

El sistema está construido principalmente bajo la arquitectura MVT (Model-View-Template) de **Django**, respaldado por una base de datos relacional **MySQL**.

## 🚀 Características Principales
- **Gestión de Inventario (CRUD):** Creación, lectura, actualización y eliminación de productos y categorías.
- **Manejo de Imágenes:** Sistema configurado para la subida, almacenamiento y renderizado de imágenes de productos en el catálogo.
- **Autenticación y Seguridad:** Sistema de login para vendedores/administradores, protegiendo las vistas de inventario interno.
- **Catálogo Público Compartible:** Interfaz amigable diseñada con Bootstrap para que los clientes puedan visualizar los productos disponibles en línea.
- **Exportación de Datos:** Funcionalidad para exportar el inventario actual en formato CSV para análisis en herramientas externas.

## ⚙️ Arquitectura y Modelado de Datos
El proyecto está dividido en aplicaciones modulares para garantizar la escalabilidad:
- `mi_tienda`: Lógica principal del negocio, autenticación y panel de administración.
- `catalogo`: Manejo de la vitrina pública, imágenes de productos y vistas de cliente.

**Entidades principales en MySQL:** `Cliente`, `Producto`, `Proveedor`, `Categoría`, `Venta`. Se implementó integridad referencial y validación de dominios para garantizar la consistencia de los datos.

## 🛠️ Instalación y Uso Local

Si deseas correr este proyecto de forma local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/felipe03441-pixel/catalogo-yams-django.git](https://github.com/felipe03441-pixel/catalogo-yams-django.git)
   cd catalogo-yams-django
