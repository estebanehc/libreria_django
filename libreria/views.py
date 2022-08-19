from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm

# Create your views here.

#ACCESO A LAS PAGINAS PRINCIPALES DEL SITIO
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


#ACCESO A LAS SECCIONES DE LA LIBRERIA
def libros (request):
    libros = Libro.objects.all() #estoy tomando todos los libros para mostrarlos
    return render(request, 'libros/index.html', {'libros': libros})

def crear (request):
    formulario = LibroForm(request.POST or None, request.FILES or None) ##igualar los formularios || files es para recibir archivos
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/crear.html', {'formulario': formulario})

def editar (request, id):
    libro = Libro.objects.get(id=id)
    formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('libros')
    return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar (request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')