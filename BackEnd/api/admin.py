from django.contrib import admin
from .models import QuejaSugerencia, ServicioCliente, ServicioUsuario, SucursalServicio, Pregunta, EvaluacionServicio
# Register your models here.


admin.site.register(QuejaSugerencia)
admin.site.register(ServicioCliente)
admin.site.register(ServicioUsuario)
admin.site.register(SucursalServicio)
admin.site.register(Pregunta)
admin.site.register(EvaluacionServicio)