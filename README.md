# Proyecto Django Simple de Gestión de Imágenes

Este es un proyecto Django sencillo que permite a los usuarios subir imágenes, crear categorías para organizarlas y gestionarlas a través de una interfaz de administración. Además, ofrece funcionalidades para editar y eliminar tanto imágenes como categorías.

## Funcionalidades Principales

* **Subida de Imágenes:** Los usuarios pueden cargar nuevas imágenes al sistema.
* **Creación de Categorías:** Se pueden crear diferentes categorías para clasificar las imágenes (ej: paisajes, retratos, animales).
* **Asignación de Categorías:** Al subir una imagen, se puede asignar a una o varias categorías existentes.
* **Interfaz de Administración:** Django Admin está configurado para gestionar fácilmente:
    * Imágenes: Ver, editar, eliminar.
    * Categorías: Crear, editar, eliminar.
* **Edición de Imágenes:** Posibilidad de modificar la información asociada a una imagen (título, descripción, categorías).
* **Eliminación de Imágenes:** Opción para eliminar imágenes del sistema.
* **Edición de Categorías:** Permite modificar el nombre y la descripción de las categorías.
* **Eliminación de Categorías:** Capacidad de eliminar categorías (se debe considerar qué sucede con las imágenes asociadas).

## Requisitos

* **Python:** Versión 3.x
* **Django:** Versión 4.x o superior (se recomienda la última estable)
* **Pillow (PIL Fork):** Para el manejo de imágenes.