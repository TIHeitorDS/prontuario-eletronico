from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from consultas.models import Consulta, Diagnostico, Prescricao, Sintoma
from consultas.serializers import (
    ConsultaSerializer,
    DiagnosticoSerializer,
    PrescricaoSerializer,
    SintomaSerializer,
)


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.select_related('paciente')
    serializer_class = ConsultaSerializer

    @action(detail=False, methods=['get'], url_path='historico')
    def historico(self, request):
        paciente_id = request.query_params.get('paciente')
        if not paciente_id:
            return Response({'detail': 'Parâmetro paciente é obrigatório.'}, status=400)
        consultas = self.get_queryset().filter(paciente_id=paciente_id).order_by('-data', '-horario')
        serializer = self.get_serializer(consultas, many=True)
        return Response(serializer.data)


class ConsultaRelacionadaViewSet(viewsets.ModelViewSet):
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
