from rest_framework import viewsets

from consultas.models import Consulta, Diagnostico, Prescricao, Sintoma
from consultas.serializers import (
    ConsultaSerializer,
    DiagnosticoSerializer,
    PrescricaoSerializer,
    SintomaSerializer,
)


class ConsultaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Consulta to be viewed or edited.
    """

    queryset = Consulta.objects.select_related('paciente')
    serializer_class = ConsultaSerializer


class ConsultaRelacionadaViewSet(viewsets.ModelViewSet):
    """Base para registros ligados a uma consulta; aceita filtro ?consulta=<id>."""

    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.query_params.get('consulta')
        if consulta:
            queryset = queryset.filter(consulta_id=consulta)
        return queryset


class SintomaViewSet(ConsultaRelacionadaViewSet):
    queryset = Sintoma.objects.all()
    serializer_class = SintomaSerializer


class DiagnosticoViewSet(ConsultaRelacionadaViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer


class PrescricaoViewSet(ConsultaRelacionadaViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer
