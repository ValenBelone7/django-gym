from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rutinas/', views.rutinas, name='rutinas'),
    
    path('socios/', views.lista_socios, name='lista_socios'),
    path('socios/crear/', views.crear_socio, name='crear_socio'),
    path('socios/editar/<int:pk>/', views.editar_socio, name='editar_socio'),
    path('socios/eliminar/<int:pk>/', views.eliminar_socio, name='eliminar_socio'),
    
    # URLs para Membresías
    path('membresias/', views.lista_membresias, name='lista_membresias'),
    path('membresias/crear/', views.crear_membresia, name='crear_membresia'),
    path('membresias/editar/<int:pk>/', views.editar_membresia, name='editar_membresia'),
    path('membresias/eliminar/<int:pk>/', views.eliminar_membresia, name='eliminar_membresia'),
]