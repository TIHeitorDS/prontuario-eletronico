from django.urls import path, include
from rest_framework import routers

from consultas.views import ConsultaViewSet, DiagnosticoViewSet, PrescricaoViewSet, SintomaViewSet

router = routers.DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register(r'sintomas', SintomaViewSet)
router.register(r'diagnosticos', DiagnosticoViewSet)
router.register(r'prescricoes', PrescricaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
