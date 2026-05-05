from django.contrib import admin
from .models import Socio, Membresia


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_filter = ['activo', 'membresia', 'fecha_inscripcion']
    search_fields = ['nombre', 'email']
    list_display = ['nombre', 'email', 'membresia', 'activo', 'fecha_inscripcion']


@admin.register(Membresia)
class MembresiaAdmin(admin.ModelAdmin):
    list_filter = ['tipo']
    search_fields = ['tipo', 'beneficios']
