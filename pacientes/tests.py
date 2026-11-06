from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pacientes.models import Paciente


class PacienteAPITestCase(APITestCase):
    def setUp(self):
        self.paciente_data = {
            'nome': 'João Silva',
            'idade': 30,
            'sexo': Paciente.Sexo.MASCULINO,
            'cpf': '12345678901',
            'estado_civil': 'Solteiro',
            'religiao': 'Católica',
            'endereco': 'Rua das Flores, 123',
            'cidade': 'Mossoró',
            'estado': 'RN',
            'telefone': '84999998888',
        }
        self.paciente = Paciente.objects.create(**self.paciente_data)
        self.list_url = reverse('paciente-list')
        self.detail_url = reverse('paciente-detail', kwargs={'pk': self.paciente.pk})

    def test_cadastrar_paciente_sucesso(self):
        """Testa o cadastro de um paciente com dados válidos."""
        novo_paciente_data = {
            'nome': 'Maria Souza',
            'idade': 25,
            'sexo': Paciente.Sexo.FEMININO,
            'cpf': '98765432100',
            'estado_civil': 'Casada',
            'religiao': 'Evangélica',
            'endereco': 'Avenida Central, 456',
            'cidade': 'Natal',
            'estado': 'RN',
            'telefone': '84988887777',
        }
        response = self.client.post(self.list_url, novo_paciente_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Paciente.objects.filter(cpf=novo_paciente_data['cpf']).exists())
        self.assertEqual(response.data['nome'], novo_paciente_data['nome'])

    def test_cadastrar_paciente_cpf_duplicado(self):
        """Testa falha de validação ao tentar cadastrar paciente com CPF já existente."""
        paciente_duplicado_data = self.paciente_data.copy()
        paciente_duplicado_data['nome'] = 'Outro Nome'
        response = self.client.post(self.list_url, paciente_duplicado_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('cpf', response.data)

    def test_listar_pacientes(self):
        """Testa a consulta/listagem de todos os pacientes."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['cpf'], self.paciente.cpf)

    def test_consultar_paciente_por_id(self):
        """Testa a consulta detalhada de um paciente específico pelo seu ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.paciente.id)
        self.assertEqual(response.data['nome'], self.paciente.nome)
        self.assertEqual(response.data['cpf'], self.paciente.cpf)

    def test_atualizar_paciente(self):
        """Testa a atualização parcial dos dados de um paciente existente."""
        dados_atualizados = {
            'telefone': '84911112222',
            'cidade': 'Tibau',
        }
        response = self.client.patch(self.detail_url, dados_atualizados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.paciente.refresh_from_db()
        self.assertEqual(self.paciente.telefone, dados_atualizados['telefone'])
        self.assertEqual(self.paciente.cidade, dados_atualizados['cidade'])

    def test_excluir_paciente(self):
        """Testa a exclusão de um paciente existente."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Paciente.objects.filter(pk=self.paciente.pk).exists())
