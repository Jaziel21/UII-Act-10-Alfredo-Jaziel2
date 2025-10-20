from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Autor
from .forms import AutorForm

def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores/listar_autores.html', {'autores': autores})

def ver_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'autores/ver_autor.html', {'autor': autor})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_autores') # Redirige al listado de autores
    else:
        form = AutorForm()
    return render(request, 'autores/agregar_autor.html', {'form': form})

def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    mensaje = None

    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            mensaje = "✅ ¡Autor editado correctamente!"
            return redirect('ver_autor', autor_id=autor.id) # Redirige a la vista del autor editado
    else:
        form = AutorForm(instance=autor)

    return render(request, 'autores/editar_autor.html', {
        'form': form,
        'mensaje': mensaje,
        'autor': autor # Para mostrar el nombre del autor en la plantilla
    })

def eliminar_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores') # Redirige al listado después de eliminar
    return render(request, 'autores/borrar_autor.html', {'autor': autor})