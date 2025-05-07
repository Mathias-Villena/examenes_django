from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, DocumentoViewSet, CarpetaViewSet, EtiquetaViewSet

router = DefaultRouter()
router.register(r'notas', NotaViewSet, basename='nota')
router.register(r'documentos', DocumentoViewSet, basename='documento')
router.register(r'carpetas', CarpetaViewSet, basename='carpeta')
router.register(r'etiquetas', EtiquetaViewSet, basename='etiqueta')

urlpatterns = [
    path('', include(router.urls)),
]