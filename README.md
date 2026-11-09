# Prontuário Eletrônico

API RESTful para gerenciamento de prontuários eletrônicos de pacientes, histórico de consultas e dados clínicos (sintomas, diagnósticos e prescrições médicas), desenvolvida com **Django** e **Django REST Framework**.

---

## 📌 Sumário

- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Instruções de Execução](#-instruções-de-execução)
  - [Pré-requisitos](#pré-requisitos)
  - [Passo a Passo](#passo-a-passo)
  - [Executando Testes](#executando-testes)
- [Descrição da API](#-descrição-da-api)
  - [Documentação Interativa (Swagger / Redoc)](#documentação-interativa-swagger--redoc)
  - [Autenticação](#autenticação)
  - [Endpoints](#endpoints)
  - [Exemplos de Uso e Payloads](#exemplos-de-uso-e-payloads)
- [Licença](#-licença)

---

## 🚀 Tecnologias Utilizadas

- **[Python](https://www.python.org/)** (v3.10+)
- **[Django](https://www.djangoproject.com/)** (v6.1+)
- **[Django REST Framework](https://www.django-rest-framework.org/)**
- **[drf-spectacular](https://drf-spectacular.readthedocs.io/)** (Documentação OpenAPI 3.0 / Swagger / ReDoc)
- **[SQLite](https://sqlite.org/)** (Banco de dados padrão para desenvolvimento)
- **[Pytest](https://docs.pytest.org/)** (Suíte de testes)

---

## 📁 Estrutura do Projeto

```text
prontuario-eletronico/
├── core/              # Configurações do projeto Django (settings, URLs, WSGI/ASGI)
├── pacientes/         # App para gerenciamento e cadastro de pacientes
├── consultas/         # App para consultas, sintomas, diagnósticos e prescrições
├── manage.py          # Utilitário de linha de comando do Django
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação do projeto
```

---

## ⚙️ Instruções de Execução

### Pré-requisitos

- **Python** 3.10 ou superior instalado na máquina.
- **Git** para versionamento.

---

### Passo a Passo

#### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/prontuario-eletronico.git
cd prontuario-eletronico
```

#### 2. Criar e ativar o ambiente virtual

- **No Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```

- **No Windows (Prompt de Comando - CMD):**
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate.bat
  ```

- **No Linux / macOS (Bash / Zsh):**
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

#### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

#### 4. Executar as migrações do banco de dados

```bash
python manage.py migrate
```

#### 5. Criar um superusuário (opcional, para acesso ao Django Admin)

```bash
python manage.py createsuperuser
```
> Siga os prompts na tela para definir usuário, e-mail e senha.

#### 6. Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

A API estará acessível em: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)  
O painel administrativo do Django estará em: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

### Executando Testes

Para executar toda a suíte de testes automatizados do projeto:

```bash
python manage.py test
```

Ou utilizando o `pytest`:

```bash
pytest
```

---

## 📖 Descrição da API

### Documentação Interativa (Swagger / Redoc)

Com o servidor em execução, você pode visualizar e interagir com a documentação interativa gerada via OpenAPI 3:

| Interface | URL | Descrição |
| --- | --- | --- |
| **Swagger UI** | `http://127.0.0.1:8000/api/schema/swagger/` | Teste interativo das rotas e visualização da especificação |
| **ReDoc** | `http://127.0.0.1:8000/api/schema/redoc/` | Documentação técnica detalhada das requisições e respostas |
| **OpenAPI Schema** | `http://127.0.0.1:8000/api/schema/` | Schema bruto da API em formato YAML/JSON |

---

### Autenticação

A API oferece suporte aos seguintes esquemas de autenticação definidos pelo Django REST Framework:
- **SessionAuthentication** (sessão do navegador/admin)
- **BasicAuthentication** (credenciais via cabeçalho HTTP `Authorization: Basic ...`)
- **TokenAuthentication** (cabeçalho HTTP `Authorization: Token <seu_token>`)

---

### Endpoints

Base URL: `http://127.0.0.1:8000/api/`

#### 1. Pacientes (`/api/pacientes/`)

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/pacientes/` | Lista todos os pacientes cadastrados |
| `POST` | `/api/pacientes/` | Cadastra um novo paciente |
| `GET` | `/api/pacientes/{id}/` | Retorna os detalhes de um paciente específico |
| `PUT` | `/api/pacientes/{id}/` | Atualiza todos os campos de um paciente |
| `PATCH` | `/api/pacientes/{id}/` | Atualiza parcialmente os dados de um paciente |
| `DELETE` | `/api/pacientes/{id}/` | Remove o paciente cadastrado |

#### 2. Consultas (`/api/consultas/`)

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/consultas/` | Lista todas as consultas |
| `POST` | `/api/consultas/` | Registra uma nova consulta médica |
| `GET` | `/api/consultas/{id}/` | Retorna os detalhes de uma consulta |
| `PUT` | `/api/consultas/{id}/` | Atualiza todos os campos de uma consulta |
| `PATCH` | `/api/consultas/{id}/` | Atualiza parcialmente os dados de uma consulta |
| `DELETE` | `/api/consultas/{id}/` | Remove uma consulta |

#### 3. Sintomas (`/api/sintomas/`)

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/sintomas/` | Lista todos os sintomas |
| `GET` | `/api/sintomas/?consulta={id}` | Filtra sintomas vinculados a uma consulta específica |
| `POST` | `/api/sintomas/` | Registra um sintoma para uma consulta |
| `GET` | `/api/sintomas/{id}/` | Retorna os detalhes de um sintoma |
| `PUT` | `/api/sintomas/{id}/` | Atualiza um sintoma |
| `PATCH` | `/api/sintomas/{id}/` | Atualiza parcialmente um sintoma |
| `DELETE` | `/api/sintomas/{id}/` | Remove um sintoma |

#### 4. Diagnósticos (`/api/diagnosticos/`)

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/diagnosticos/` | Lista todos os diagnósticos |
| `GET` | `/api/diagnosticos/?consulta={id}` | Filtra diagnósticos vinculados a uma consulta |
| `POST` | `/api/diagnosticos/` | Registra um diagnóstico para uma consulta |
| `GET` | `/api/diagnosticos/{id}/` | Retorna os detalhes de um diagnóstico |
| `PUT` | `/api/diagnosticos/{id}/` | Atualiza um diagnóstico |
| `PATCH` | `/api/diagnosticos/{id}/` | Atualiza parcialmente um diagnóstico |
| `DELETE` | `/api/diagnosticos/{id}/` | Remove um diagnóstico |

#### 5. Prescrições (`/api/prescricoes/`)

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/prescricoes/` | Lista todas as prescrições médicas |
| `GET` | `/api/prescricoes/?consulta={id}` | Filtra prescrições vinculadas a uma consulta |
| `POST` | `/api/prescricoes/` | Registra uma nova prescrição médica |
| `GET` | `/api/prescricoes/{id}/` | Retorna os detalhes de uma prescrição |
| `PUT` | `/api/prescricoes/{id}/` | Atualiza uma prescrição |
| `PATCH` | `/api/prescricoes/{id}/` | Atualiza parcialmente uma prescrição |
| `DELETE` | `/api/prescricoes/{id}/` | Remove uma prescrição |

---

### Exemplos de Uso e Payloads

#### Criar Paciente (`POST /api/pacientes/`)

**Payload:**
```json
{
  "nome": "João Silva",
  "idade": 32,
  "sexo": "M",
  "cpf": "12345678901",
  "estado_civil": "Solteiro",
  "religiao": "Católica",
  "endereco": "Rua das Flores, 123",
  "cidade": "Mossoró",
  "estado": "RN",
  "telefone": "84999998888"
}
```
*Obs: O campo `sexo` aceita `'M'` (Masculino), `'F'` (Feminino) ou `'O'` (Outro). O campo `cpf` deve ser único.*

---

#### Agendar Consulta (`POST /api/consultas/`)

**Payload:**
```json
{
  "paciente": 1,
  "data": "2026-12-01",
  "horario": "09:30:00",
  "descricao": "Consulta de rotina cardiológica"
}
```

---

#### Cadastrar Sintoma (`POST /api/sintomas/`)

**Payload:**
```json
{
  "consulta": 1,
  "descricao": "Febre alta e tosse seca persistente"
}
```

---

#### Cadastrar Diagnóstico (`POST /api/diagnosticos/`)

**Payload:**
```json
{
  "consulta": 1,
  "descricao": "Quadro infeccioso viral das vias respiratórias superiores (Gripe A)."
}
```

---

#### Cadastrar Prescrição (`POST /api/prescricoes/`)

**Payload:**
```json
{
  "consulta": 1,
  "medicamento": "Paracetamol",
  "dosagem": "750mg",
  "instrucoes": "Tomar 1 comprimido por via oral a cada 8 horas em caso de febre ou dor."
}
```

---

#### Filtrar Registros por Consulta

Para recuperar os sintomas, diagnósticos ou prescrições de uma determinada consulta:

```bash
# Sintomas da consulta com ID 1
curl http://127.0.0.1:8000/api/sintomas/?consulta=1

# Prescrições da consulta com ID 1
curl http://127.0.0.1:8000/api/prescricoes/?consulta=1
```

---

## 📄 Licença

Este projeto é distribuído sob os termos da licença [MIT](LICENSE).
