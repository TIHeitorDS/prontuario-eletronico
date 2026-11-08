from rest_framework import serializers

from consultas.models import Consulta, Diagnostico, Prescricao, Sintoma


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def validate(self, attrs):
        paciente = attrs.get('paciente') or getattr(self.instance, 'paciente', None)
        data = attrs.get('data') or getattr(self.instance, 'data', None)
        horario = attrs.get('horario') or getattr(self.instance, 'horario', None)

        if paciente and data and horario:
            qs = Consulta.objects.filter(paciente=paciente, data=data, horario=horario)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError(
                    {'non_field_errors': ['Já existe outra consulta marcada para o mesmo paciente no mesmo horário.']}
                )

        return attrs


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
