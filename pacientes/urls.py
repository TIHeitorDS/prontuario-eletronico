from django.urls import path, include
from rest_framework import routers

from pacientes.views import PacienteViewSet

router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]