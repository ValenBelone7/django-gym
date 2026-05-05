from django.db import models


class Membresia(models.Model):
    TIPO_CHOICES = [
        ('BASICO', 'Básico'),
        ('PREMIUM', 'Premium'),
        ('VIP', 'VIP'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion_meses = models.IntegerField()
    beneficios = models.TextField()

    def __str__(self):
        return f"{self.tipo} - ${self.precio}"


class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
