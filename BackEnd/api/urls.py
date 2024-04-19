from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'QuejaSugerencia',views.QuejaSugerenciaViewSet)
router.register(r'ServicioCliente',views.ServicioClienteViewSet)
router.register(r'ServicioUsuario',views.ServicioUsuarioViewSet)
router.register(r'SucursalServicio',views.SucursalServicioViewSet)
router.register(r'Pregunta',views.PreguntaViewSet)
router.register(r'EvaluacionServicio',views.EvaluacionServicioViewSet)


urlpatterns = [
    path('', include(router.urls))
]