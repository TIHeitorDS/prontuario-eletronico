from rest_framework import serializers

from consultas.models import Consulta, Diagnostico, Prescricao, Sintoma


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class SintomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintoma
        fields = '__all__'


class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'


class PrescricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescricao
        fields = '__all__'
