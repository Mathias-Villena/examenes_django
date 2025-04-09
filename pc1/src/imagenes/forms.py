from django import forms
from .models import Imagen, Categoria

class ImagenForm(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['titulo', 'descripcion', 'archivo', 'categoria']
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']