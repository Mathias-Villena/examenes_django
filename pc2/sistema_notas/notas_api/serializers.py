from rest_framework import serializers
from .models import Nota, Documento, Carpeta, Etiqueta

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ['id', 'nombre', 'color']

class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpeta
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion']
        read_only_fields = ['usuario']

class NotaSerializer(serializers.ModelSerializer):
    etiquetas = EtiquetaSerializer(many=True, read_only=True)

    class Meta:
        model = Nota
        fields = ['id', 'titulo', 'contenido', 'carpeta', 'etiquetas',
                 'fecha_creacion', 'fecha_modificacion', 'compartido_con']
        read_only_fields = ['usuario', 'fecha_creacion', 'fecha_modificacion']

class DocumentoSerializer(serializers.ModelSerializer):
    etiquetas = EtiquetaSerializer(many=True, read_only=True)

    class Meta:
        model = Documento
        fields = ['id', 'nombre', 'archivo', 'descripcion', 'carpeta',
                 'etiquetas', 'fecha_subida', 'compartido_con']
        read_only_fields = ['usuario', 'fecha_subida']