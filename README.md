# Sistema de Agendamentos

Este sistema permite o agendamento de horários para profissionais, com persistência de dados em banco MySQL e arquitetura baseada em containers Docker.

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

1. Clone o repositório
```bash
git clone https://github.com/pamelaiwabuchi/sistema-agendamentos.git
cd sistema-agendamentos
```
2. Configure as variáveis de ambiente
Este projeto utiliza um arquivo de configuração para gerenciar as credenciais do banco de dados.
```bash
cp .env.example .env
```
Abra o arquivo .env com um editor de texto de sua preferência e preencha o campo DB_PASSWORD com a senha desejada para o banco de dados.

3. Suba o sistema
```bash
docker compose up -d --build
#ou, dependendo da sua versão:
docker-compose up -d --build
```

4. Acesse a aplicação:

O sistema estará disponível em: http://localhost:5001

## Persistência de Dados

O sistema implementa **Volumes Docker** para a persistência de dados. Isso garante que as informações salvas no banco de dados sejam preservadas no disco físico, mantendo a integridade dos agendamentos mesmo após a interrupção dos containers.

## Ambiente de Deploy

O projeto está hospedado em uma instância da AWS (Amazon Web Services). A arquitetura em containers permite que a aplicação seja escalável e pronta para execução em ambiente de produção, mantendo a paridade com o ambiente local. 

*Desenvolvido como parte das atividades práticas da matéria de Desenvolvimento web - FATEC.*