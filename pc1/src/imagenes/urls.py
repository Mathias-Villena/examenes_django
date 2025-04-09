from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_imagenes, name='lista_imagenes'),
    path('imagen/<int:pk>/', views.detalle_imagen, name='detalle_imagen'),
    path('subir/', views.subir_imagen, name='subir_imagen'),
    path('eliminar/<int:pk>/', views.eliminar_imagen, name='eliminar_imagen'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria/<slug:slug>/', views.imagenes_por_categoria, name='imagenes_por_categoria'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
]