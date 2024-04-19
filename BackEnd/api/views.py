from rest_framework import viewsets
from .serializer import QuejaSugerenciaSerializer, ServicioClienteSerializer, ServicioUsuarioSerializer,SucursalServicioSerializer, PreguntaSerializer, EvaluacionServicioSerializer
from .models import QuejaSugerencia, ServicioCliente, ServicioUsuario, SucursalServicio, Pregunta, EvaluacionServicio


# Create your views here.
class QuejaSugerenciaViewSet(viewsets.ModelViewSet):
    queryset = QuejaSugerencia.objects.all()
    serializer_class = QuejaSugerenciaSerializer


class ServicioClienteViewSet(viewsets.ModelViewSet):
    queryset = ServicioCliente.objects.all()
    serializer_class = ServicioClienteSerializer
    
class ServicioUsuarioViewSet(viewsets.ModelViewSet):
    queryset = ServicioUsuario.objects.all()
    serializer_class = ServicioUsuarioSerializer
    
    
class SucursalServicioViewSet(viewsets.ModelViewSet):
    queryset = SucursalServicio.objects.all()
    serializer_class = SucursalServicioSerializer
    
class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    
class EvaluacionServicioViewSet(viewsets.ModelViewSet):
    queryset = EvaluacionServicio.objects.all()
    serializer_class = EvaluacionServicioSerializer