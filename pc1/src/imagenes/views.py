from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Imagen, Categoria
from .forms import ImagenForm, CategoriaForm

def lista_imagenes(request):
    imagenes = Imagen.objects.all().order_by('-fecha_subida')
    return render(request, 'imagenes/lista_imagenes.html', {'imagenes': imagenes})

def detalle_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    imagen.visualizaciones += 1  # Incrementa el contador
    imagen.save()  # Guarda el cambio
    return render(request, 'imagenes/detalle_imagen.html', {'imagen': imagen})

@login_required
def subir_imagen(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = form.save(commit=False)
            imagen.usuario = request.user
            imagen.save()
            messages.success(request, '¡Imagen subida correctamente!')
            return redirect('detalle_imagen', pk=imagen.pk)
    else:
        form = ImagenForm()
    
    return render(request, 'imagenes/subir_imagen.html', {'form': form})

@login_required
def eliminar_imagen(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk, usuario=request.user)
    
    if request.method == 'POST':
        imagen.delete()
        messages.success(request, '¡Imagen eliminada correctamente!')
        return redirect('lista_imagenes')
    
    return render(request, 'imagenes/eliminar_imagen.html', {'imagen': imagen})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'imagenes/categorias.html', {'categorias': categorias})

def imagenes_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    imagenes = Imagen.objects.filter(categoria=categoria).order_by('-fecha_subida')
    return render(request, 'imagenes/imagenes_por_categoria.html', {
        'categoria': categoria,
        'imagenes': imagenes
    })

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría creada correctamente!')
            return redirect('categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'imagenes/crear_categoria.html', {'form': form})
