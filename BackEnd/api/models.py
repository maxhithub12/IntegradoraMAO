from django.db import models

# Create your models here.



class QuejaSugerencia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    estatus_choices = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Resuelto', 'Resuelto'),
    ]
    estatus = models.CharField(max_length=20, choices=estatus_choices)
    tipo_choices = [
        ('Queja', 'Queja'),
        ('Sugerencia', 'Sugerencia'),
    ]
    tipo = models.CharField(max_length=20, choices=tipo_choices)
    persona_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla personas

    class Meta:
        db_table = 'quejas_sugerencias'

    def __str__(self):
        return f"ID: {self.id}, Tipo: {self.tipo}, Estatus: {self.estatus}"



class ServicioCliente(models.Model):
    nombre_servicio = models.CharField(max_length=50, null=True)
    disponibilidad_choices = [
        ('Disponible', 'Disponible'),
        ('No disponible', 'No disponible'),
    ]
    disponibilidad = models.CharField(max_length=20, choices=disponibilidad_choices, null=True)
    descripcion = models.TextField()
    instructor_id = models.PositiveIntegerField(null=True)
    sucursal_id = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = 'servicio_al_cliente'

    def __str__(self):
        return f"ID: {self.id}, Nombre del Servicio: {self.nombre_servicio}, Disponibilidad: {self.disponibilidad}"


class ServicioUsuario(models.Model):
    miembros_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla miembros
    servicio_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla servicio_al_cliente
    empleado_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla empleados
    fecha_de_uso = models.DateField(null=True)
    tiempo_uso = models.TimeField(null=True)

    class Meta:
        db_table = 'servicios_usuarios'

    def __str__(self):
        return f"ID de Miembro: {self.miembros_id}, ID de Servicio: {self.servicio_id}, ID de Empleado: {self.empleado_id}"
    


class SucursalServicio(models.Model):
    sucursal_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla sucursales
    servicio_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla servicio_al_cliente
    estatus_choices = [
        ('Disponible', 'Disponible'),
        ('No disponible', 'No disponible'),
    ]
    estatus = models.CharField(max_length=20, choices=estatus_choices, null=True)

    class Meta:
        db_table = 'sucursales_servicios'

    def __str__(self):
        return f"ID de Sucursal: {self.sucursal_id}, ID de Servicio: {self.servicio_id}, Estatus: {self.estatus}"
    
    
    
 # Definimos las opciones fuera de la clase Pregunta
TIPO_CHOICES = [
    ('Abierta', 'Abierta'),
    ('Cerrada', 'Cerrada'),
]

class Pregunta(models.Model):
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, null=True)
    persona_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla personas

    class Meta:
        db_table = 'pregunta'

    def __str__(self):
        return f"ID de Pregunta: {self.id}, Tipo: {self.tipo}"
    
    
class EvaluacionServicio(models.Model):
    servicio_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla servicio_al_cliente
    comentarios = models.TextField(null=True)
    fecha_registro = models.DateField(null=True)
    puntuacion_choices = [
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo'),
    ]
    puntuacion = models.CharField(max_length=20, choices=puntuacion_choices, null=True)
    persona_id = models.PositiveIntegerField(null=True)  # Llave foránea a la tabla personas

    class Meta:
        db_table = 'evaluacion_servicio'

    def __str__(self):
        return f"ID de Servicio: {self.servicio_id}, Puntuación: {self.puntuacion}"
    
    
class test(models.Model):
    comentarios = models.TextField(null=True)
    fecha_registro = models.DateField(null=True)
   

    
    