from datetime import date, time

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from consultas.models import Consulta, Sintoma
from pacientes.models import Paciente


class ConsultaAPITestCase(APITestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nome='João Silva', idade=30, sexo='M', cpf='12345678901',
            endereco='Rua A, 1', cidade='Mossoró', estado='RN', telefone='84999998888',
        )
        self.consulta = Consulta.objects.create(
            paciente=self.paciente, data=date(2026, 12, 1), horario=time(9, 0), descricao='Rotina',
        )
        self.list_url = reverse('consulta-list')
        self.detail_url = reverse('consulta-detail', kwargs={'pk': self.consulta.pk})

    def payload(self, **kw):
        base = {'paciente': self.paciente.pk, 'data': '2026-12-01', 'horario': '10:00:00', 'descricao': 'Retorno'}
        base.update(kw)
        return base

    def test_cadastrar_consulta(self):
        response = self.client.post(self.list_url, self.payload(), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Consulta.objects.count(), 2)

    def test_atualizar_consulta(self):
        response = self.client.patch(self.detail_url, {'descricao': 'Nova'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_listar_consultar_excluir(self):
        self.assertEqual(self.client.get(self.list_url).status_code, 200)
        self.assertEqual(self.client.get(self.detail_url).status_code, 200)
        self.assertEqual(self.client.delete(self.detail_url).status_code, 204)


class RegistrosDaConsultaAPITestCase(APITestCase):
    def setUp(self):
        paciente = Paciente.objects.create(
            nome='João Silva', idade=30, sexo='M', cpf='12345678901',
            endereco='Rua A, 1', cidade='Mossoró', estado='RN', telefone='84999998888',
        )
        self.consulta = Consulta.objects.create(
            paciente=paciente, data=date(2026, 12, 1), horario=time(9, 0), descricao='Rotina',
        )
        self.outra = Consulta.objects.create(
            paciente=paciente, data=date(2026, 12, 2), horario=time(9, 0), descricao='Retorno',
        )

    def crud(self, basename, dados, campo_update):
        list_url = reverse(f'{basename}-list')
        response = self.client.post(list_url, dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        detail_url = reverse(f'{basename}-detail', kwargs={'pk': response.data['id']})
        self.assertEqual(self.client.get(detail_url).status_code, status.HTTP_200_OK)
        response = self.client.patch(detail_url, campo_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.delete(detail_url).status_code, status.HTTP_204_NO_CONTENT)

    def test_crud_sintoma(self):
        self.crud('sintoma', {'consulta': self.consulta.pk, 'descricao': 'Febre'}, {'descricao': 'Tosse'})

    def test_crud_diagnostico(self):
        self.crud('diagnostico', {'consulta': self.consulta.pk, 'descricao': 'Gripe'}, {'descricao': 'Resfriado'})

    def test_crud_prescricao(self):
        dados = {
            'consulta': self.consulta.pk, 'medicamento': 'Paracetamol',
            'dosagem': '500mg', 'instrucoes': '1 comprimido a cada 8h',
        }
        self.crud('prescricao', dados, {'dosagem': '750mg'})

    def test_prescricao_exige_campos(self):
        response = self.client.post(reverse('prescricao-list'), {'consulta': self.consulta.pk}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        for campo in ('medicamento', 'dosagem', 'instrucoes'):
            self.assertIn(campo, response.data)

    def test_filtrar_sintomas_por_consulta(self):
        Sintoma.objects.create(consulta=self.consulta, descricao='Febre')
        Sintoma.objects.create(consulta=self.outra, descricao='Dor')
        response = self.client.get(reverse('sintoma-list'), {'consulta': self.consulta.pk})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['descricao'], 'Febre')
