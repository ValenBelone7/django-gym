from django.shortcuts import render
from .models import Socio

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