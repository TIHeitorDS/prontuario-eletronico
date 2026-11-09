from pacientes.models import Paciente
from rest_framework import serializers


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"