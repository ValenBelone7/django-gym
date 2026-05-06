from django.shortcuts import render, redirect, get_object_or_404
from .models import Socio, Membresia
from .forms import SocioForm, MembresiaForm


def home(request):
    beneficios = ['Equipamiento moderno', 'Profesores certificados', 'Clases grupales', 'Planes personalizados']
    total_socios = Socio.objects.filter(activo=True).count()
    return render(request, 'gimnasio/home.html', {
        'total_socios': total_socios,
        'beneficios': beneficios,
    })


def rutinas(request):
    rutinas = [
        {'dia': 'Lunes', 'grupo': 'Pecho y Tríceps', 'nivel': 'Intermedio'},
        {'dia': 'Miércoles', 'grupo': 'Espalda y Bíceps', 'nivel': 'Avanzado'},
        {'dia': 'Viernes', 'grupo': 'Piernas y Hombros', 'nivel': 'Básico'},
        {'dia': 'Sábado', 'grupo': 'Cardio y Core', 'nivel': 'Básico'},
    ]
    return render(request, 'gimnasio/rutinas.html', {'rutinas': rutinas})

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'gimnasio/socios/lista.html', {'socios': socios})


def crear_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = SocioForm()
    return render(request, 'gimnasio/socios/form.html', {'form': form, 'titulo': 'Crear Socio'})


def editar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'gimnasio/socios/form.html', {'form': form, 'titulo': 'Editar Socio'})


def eliminar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == 'POST':
        socio.delete()
        return redirect('lista_socios')
    return render(request, 'gimnasio/socios/confirmar_eliminar.html', {'socio': socio})


def lista_membresias(request):
    membresias = Membresia.objects.all()
    return render(request, 'gimnasio/membresias/lista.html', {'membresias': membresias})


def crear_membresia(request):
    if request.method == 'POST':
        form = MembresiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_membresias')
    else:
        form = MembresiaForm()
    return render(request, 'gimnasio/membresias/form.html', {'form': form, 'titulo': 'Crear Membresía'})


def editar_membresia(request, pk):
    membresia = get_object_or_404(Membresia, pk=pk)
    if request.method == 'POST':
        form = MembresiaForm(request.POST, instance=membresia)
        if form.is_valid():
            form.save()
            return redirect('lista_membresias')
    else:
        form = MembresiaForm(instance=membresia)
    return render(request, 'gimnasio/membresias/form.html', {'form': form, 'titulo': 'Editar Membresía'})


def eliminar_membresia(request, pk):
    membresia = get_object_or_404(Membresia, pk=pk)
    if request.method == 'POST':
        membresia.delete()
        return redirect('lista_membresias')
    return render(request, 'gimnasio/membresias/confirmar_eliminar.html', {'membresia': membresia})
