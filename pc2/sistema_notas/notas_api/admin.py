from django.contrib import admin
from .models import Nota, Documento, Carpeta, Etiqueta

@admin.register(Carpeta)
class CarpetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'carpeta', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('titulo', 'contenido')
    list_filter = ('carpeta', 'etiquetas', 'fecha_creacion')
    filter_horizontal = ('etiquetas',)

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'carpeta', 'fecha_subida')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('carpeta', 'fecha_subida')

@admin.register(Etiqueta)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'color')
    search_fields = ('nombre',)