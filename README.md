# Projeto FastAPI - Sistema de Ordens de Serviço

Este projeto é uma aplicação web construída com **FastAPI**, que permite gerenciar Ordens de Serviço (OS) para clientes, incluindo funcionalidades como criação de novas ordens, gerenciamento de clientes e serviços, e controle de status das ordens. O projeto utiliza o FastAPI para a construção da API, com um banco de dados para armazenar as informações.

## Tecnologias Usadas

- **FastAPI** - Framework para desenvolvimento de APIs rápidas e eficientes.
- **Uvicorn** - Servidor ASGI para rodar a aplicação FastAPI.
- **SQLAlchemy** - ORM para interação com o banco de dados.
- **SQLite** - Banco de dados relacional (pode ser substituído por outros, como PostgreSQL ou MySQL, conforme necessidade).
- **Pydantic** - Biblioteca para validação e serialização de dados.
- **Jinja2** - Motor de templates para renderização de HTML.
- **Git** - Controle de versão.

## Funcionalidades

- **Criação de Ordens de Serviço**: Permite que os usuários registrem novas ordens para clientes.
- **Cadastro de Clientes**: Possibilita o gerenciamento de informações dos clientes.
- **Gestão de Status**: Acompanhe o andamento das ordens de serviço com status como "Em andamento", "Concluída", etc.
- **Autenticação de Usuários**: (Ainda não implementado) Protege rotas para acesso restrito.


## Instalação

1. Clone o repositório para o seu diretório local:
   ```bash
   git clone https://codeberg.org/seu_usuario/Python_FastAPI.git

   Navegue até o diretório do projeto:
   cd Python_FastAPI
   
   Crie um ambiente virtual:
   python3 -m venv venv
   source venv/bin/activate  # Para Linux/MacOS
   venv\Scripts\activate     # Para Windows

   Instale as dependências:
   pip install -r requirements.txt

   Para rodar a aplicação:
   uvicorn main:app --reload


