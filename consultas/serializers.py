from datetime import date

from rest_framework import serializers

from consultas.models import Consulta, Diagnostico, Prescricao, Sintoma


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def validate_data(self, value):
        """Regra de negócio: não é possível agendar consultas em datas passadas."""
        if value < date.today():
            raise serializers.ValidationError('Não é possível agendar consulta em data passada.')
        return value

    def validate(self, attrs):
        """Regra de negócio: um paciente não pode ter duas consultas no mesmo dia e horário."""
        atual = self.instance
        paciente = attrs.get('paciente', atual.paciente if atual else None)
        data = attrs.get('data', atual.data if atual else None)
        horario = attrs.get('horario', atual.horario if atual else None)
        conflitos = Consulta.objects.filter(paciente=paciente, data=data, horario=horario)
        if atual:
            conflitos = conflitos.exclude(pk=atual.pk)
        if conflitos.exists():
            raise serializers.ValidationError('O paciente já possui uma consulta neste dia e horário.')
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
