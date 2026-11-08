from django.urls import include, path
from rest_framework.routers import DefaultRouter

from consultas.views import ConsultaViewSet, DiagnosticoViewSet, PrescricaoViewSet, SintomaViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)
router.register(r'sintomas', SintomaViewSet)
router.register(r'diagnosticos', DiagnosticoViewSet)
router.register(r'prescricoes', PrescricaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
