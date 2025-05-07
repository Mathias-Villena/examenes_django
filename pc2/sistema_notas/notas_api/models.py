from django.db import models
from django.contrib.auth.models import User
class Carpeta(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carpetas', null=True)  # Añadimos null=True

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#000000')  # Para códigos de color hex

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, related_name='notas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    etiquetas = models.ManyToManyField('Etiqueta', blank=True)
    compartido_con = models.ManyToManyField(User, related_name='notas_compartidas', blank=True)

    def __str__(self):
        return self.titulo

class Documento(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    descripcion = models.TextField(blank=True, null=True)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, related_name='documentos')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    etiquetas = models.ManyToManyField('Etiqueta', blank=True)
    compartido_con = models.ManyToManyField(User, related_name='documentos_compartidos', blank=True)

    def __str__(self):
        return self.nombre