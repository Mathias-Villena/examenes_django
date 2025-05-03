from django.contrib import admin
from .models import Categoria, Imagen

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    search_fields = ('nombre',)
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'usuario', 'fecha_subida','visualizaciones')
    list_filter = ('categoria', 'fecha_subida', 'usuario')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'fecha_subida'