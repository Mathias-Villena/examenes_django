from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre

class Imagen(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    archivo = models.ImageField(upload_to='imagenes/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='imagenes')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imagenes')
    visualizaciones = models.PositiveIntegerField(default=0)  # Nuevo campo
    def __str__(self):
        return self.titulo