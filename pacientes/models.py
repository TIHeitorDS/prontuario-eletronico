from django.db import models


class Paciente(models.Model):
    class Sexo(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
        OUTRO = 'O', 'Outro'

    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=Sexo.choices)
    cpf = models.CharField(max_length=11, unique=True)
    estado_civil = models.CharField(max_length=20, blank=True, null=True)
    religiao = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
