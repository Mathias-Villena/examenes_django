from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default="#000000")

    def __str__(self):
        return self.nombre

class Carpeta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.SET_NULL, null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    compartido_con = models.ManyToManyField(User, related_name='notas_compartidas', blank=True)

    def __str__(self):
        return self.titulo

class Documento(models.Model):
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    descripcion = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.SET_NULL, null=True, blank=True)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    compartido_con = models.ManyToManyField(User, related_name='documentos_compartidos', blank=True)

    def __str__(self):
        return self.nombre