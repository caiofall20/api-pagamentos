# API de Pagamentos - README

Este é um projeto de API de pagamentos desenvolvido em Django REST framework para simular pagamentos. Ele permite criar contas, verificar saldo, enviar pagamentos e listar informações de pagamento. A seguir, você encontrará instruções sobre como configurar e testar o projeto.

## Pré-requisitos

- Python 3.7 ou superior
- Ambiente virtual (recomendado)

## Configuração do Projeto

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto

2.Criando e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
```

3.Criando e ative um ambiente virtual

```bash
pip install -r requirements.txt
```

3.Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

3.Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

## Rotas da API

Aqui estão as principais rotas da API:

### Criar Conta

Crie uma conta fornecendo o número, nome e saldo da conta.

- Rota: `POST /api/criar-conta/`
- Exemplo de JSON:

  ```json
  {
      "numero": "1234567891",
      "nome": "Exemplo",
      "saldo": 1000.00
  }

### Verificar Saldo

Consulte o saldo de uma conta pelo número.

- Rota: `GET /api/saldo/<numero-da-conta>/`
- Exemplo de JSON de resposta:

  ```json
  {
      "saldo": 1000.00
  }

### Enviar Pagamento

Consulte o saldo de uma conta pelo número.

- Rota: `POST /api/enviar-pagamento/<numero-da-conta>/`
- Exemplo de JSON de resposta:

  ```json
  {
      
    "valor": 500.00,
    "beneficiario": "Nome do Beneficiário"

  }
