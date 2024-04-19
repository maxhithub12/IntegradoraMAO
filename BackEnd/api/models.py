from django.db import models

# Create your models here.
class Persona(models.Model):
    Titulo_Cortesia = models.CharField(max_length=20, null=True)
    Nombre = models.CharField(max_length=80)
    Primer_Apellido = models.CharField(max_length=80)
    Segundo_Apellido = models.CharField(max_length=80)
    Fecha_Nacimiento = models.DateField()
    Fotografia = models.CharField(max_length=100, null=True)
    Genero_choices = [('M', 'Masculino'), ('F', 'Femenino'), ('N/B', 'No binario')]
    Genero = models.CharField(max_length=3, choices=Genero_choices, null=True)
    Tipo_Sangre_choices = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')]
    Tipo_Sangre = models.CharField(max_length=3, choices=Tipo_Sangre_choices)
    Estatus = models.BooleanField(default=True)
    Fecha_Registro = models.DateTimeField(auto_now_add=True)
    Fecha_Actualizacion = models.DateTimeField(null=True)
    