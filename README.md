# Sistema de Agendamentos

Este sistema permite o agendamento de horários para profissionais, com persistência de dados em banco MySQL e arquitetura baseada em containers Docker.

## Estrutura do Projeto

```
├── 📁 static
├── 📁 templates
│   └── 🌐 index.html
├── ⚙️ .env.example
├── ⚙️ .gitignore
├── 🐳 Dockerfile
├── 📝 README.md
├── 🐍 app.py
├── ⚙️ docker-compose.yml
├── 📄 requirements.txt
└── 📄 script.sql
```
---

## Tecnologias utilizadas
- Backend: Python (Flask)
- Banco de Dados: MySQL 8.0
- Frontend: HTML5, JavaScript, Tailwind CSS
- Infraestrutura: Docker, Docker Compose e AWS (Amazon Web Services)

## Pré-Requisitos
Para executar este projeto, você precisará das seguintes ferramentas instaladas:

Docker Desktop: Instale a versão correspondente ao seu sistema operacional (Windows, Linux ou macOS). 
Git: Para clonar o repositório.

## Como executar (Guia do Usuário)

Opção 1: Ideal para visualizar o código e realizar alterações.

```bash
git clone https://github.com/pamelaiwabuchi/sistema-agendamentos.git
cd sistema-agendamentos
cp .env.example .env
# Edite o .env com sua senha
docker-compose up -d --build
```

Opção 2: Execução Rápida (Produção/Docker Hub)
Ideal para rodar o sistema rapidamente utilizando a imagem oficial.

```bash
git clone https://github.com/pamelaiwabuchi/sistema-agendamentos.git
cd sistema-agendamentos
cp .env.example .env
# Edite o .env com sua senha
docker-compose pull
docker-compose up -d
```

## Persistência de Dados

O sistema implementa **Volumes Docker** para a persistência de dados. Isso garante que as informações salvas no banco de dados sejam preservadas no disco físico, mantendo a integridade dos agendamentos mesmo após a interrupção dos containers.

## Ambiente de Deploy

O projeto está hospedado em uma instância da AWS (Amazon Web Services). A arquitetura em containers permite que a aplicação seja escalável e pronta para execução em ambiente de produção, mantendo a paridade com o ambiente local. 

Para instruções de uso do sistema, consulte o Guia do Usuário.

*Desenvolvido como parte das atividades práticas da matéria de Desenvolvimento web - FATEC.*