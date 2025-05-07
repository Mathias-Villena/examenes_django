from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotaViewSet, DocumentoViewSet, CarpetaViewSet, EtiquetaViewSet

router = DefaultRouter()
router.register('carpetas', CarpetaViewSet, basename='carpeta')
router.register('notas', NotaViewSet, basename='nota')
router.register('documentos', DocumentoViewSet, basename='documento')
router.register('etiquetas', EtiquetaViewSet, basename='etiqueta')

urlpatterns = [
    path('', include(router.urls)),
]