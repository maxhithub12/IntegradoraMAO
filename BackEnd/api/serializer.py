from rest_framework import serializers
from .models import QuejaSugerencia, ServicioCliente, ServicioUsuario, SucursalServicio, Pregunta, EvaluacionServicio

class QuejaSugerenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuejaSugerencia
        fields = '__all__'
        
class ServicioClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServicioCliente
        fields = '__all__'
        
class ServicioUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServicioUsuario
        fields = '__all__'
        
class SucursalServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=SucursalServicio
        fields = '__all__'
    
class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pregunta
        fields = '__all__'
        
class EvaluacionServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model=EvaluacionServicio
        fields = '__all__'