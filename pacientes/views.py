from rest_framework import viewsets
from pacientes.models import Paciente
from pacientes.serializers import PacienteSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Paciente to be viewed or edited.
    """
    
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer