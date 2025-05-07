from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny  # Añade esta línea
from django_filters.rest_framework import DjangoFilterBackend
from .models import Nota, Documento, Carpeta, Etiqueta
from .serializers import NotaSerializer, DocumentoSerializer, CarpetaSerializer, EtiquetaSerializer
from django.contrib.auth.models import User

class NotaViewSet(viewsets.ModelViewSet):
    serializer_class = NotaSerializer
    permission_classes = [AllowAny]  # Cambia esto
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['titulo', 'contenido']
    filterset_fields = ['carpeta', 'etiquetas']
    queryset = Nota.objects.all()  # Añade esta línea

class DocumentoViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentoSerializer
    permission_classes = [AllowAny]  # Cambia esto
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'descripcion']
    filterset_fields = ['carpeta', 'etiquetas']
    queryset = Documento.objects.all()  # Añade esta línea

class CarpetaViewSet(viewsets.ModelViewSet):
    queryset = Carpeta.objects.all()
    serializer_class = CarpetaSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Obtener el primer usuario o crear uno si no existe
        usuario, created = User.objects.get_or_create(username='default_user')
        serializer.save(usuario=usuario)

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer
    permission_classes = [AllowAny]  # Cambia esto