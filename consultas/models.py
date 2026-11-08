from django.core.exceptions import ValidationError
from django.db import models

from pacientes.models import Paciente


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateField()
    horario = models.TimeField()
    descricao = models.TextField()

    class Meta:
        ordering = ['data', 'horario']
        constraints = [
            models.UniqueConstraint(
                fields=['paciente', 'data', 'horario'],
                name='unique_consulta_paciente_data_horario',
            )
        ]

    def __str__(self):
        return f'{self.paciente} - {self.data} {self.horario}'

    def clean(self):
        super().clean()
        if self.paciente_id and self.data and self.horario:
            same_time = Consulta.objects.filter(
                paciente_id=self.paciente_id,
                data=self.data,
                horario=self.horario,
            ).exclude(pk=self.pk)
            if same_time.exists():
                raise ValidationError('Já existe outra consulta marcada para este paciente no mesmo horário.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Sintoma(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='sintomas')
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao


class Diagnostico(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='diagnosticos')
    descricao = models.TextField()

    def __str__(self):
        return self.descricao[:50]


class Prescricao(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='prescricoes')
    medicamento = models.CharField(max_length=100)
    dosagem = models.CharField(max_length=100)
    instrucoes = models.TextField()

    class Meta:
        verbose_name_plural = 'prescrições'

    def __str__(self):
        return f'{self.medicamento} ({self.dosagem})'
