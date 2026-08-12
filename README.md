# CodeFactory TaskManager

![CI](https://github.com/Jessica-NC/DevOps/actions/workflows/ci.yml/badge.svg)

> Projeto demonstrativo desenvolvido como parte da adoÃ§Ã£o da Cultura DevOps na
> CodeFactory Solutions (Atividade PrÃ¡tica â€” DevOps e IntegraÃ§Ã£o ContÃ­nua, UNINTER).

## DescriÃ§Ã£o do projeto

O **CodeFactory TaskManager** Ã© uma API REST simples de gerenciamento de
tarefas, utilizada como projeto de referÃªncia para demonstrar, na prÃ¡tica,
a adoÃ§Ã£o da Cultura DevOps pela equipe da CodeFactory Solutions:
versionamento com Git/GitHub, containerizaÃ§Ã£o com Docker e um pipeline de
IntegraÃ§Ã£o ContÃ­nua.

## Objetivo

Demonstrar como prÃ¡ticas e ferramentas de DevOps (controle de versÃ£o
colaborativo, containers e automaÃ§Ã£o de build/testes) podem resolver os
problemas de padronizaÃ§Ã£o, integraÃ§Ã£o e agilidade enfrentados pela equipe
de desenvolvimento da CodeFactory Solutions.

## Tecnologias utilizadas

- Python 3.12 + Flask (API REST)
- Flask-SQLAlchemy (ORM)
- PostgreSQL (banco de dados em produÃ§Ã£o/Docker)
- SQLite (banco em memÃ³ria para testes)
- Docker e Docker Compose (containerizaÃ§Ã£o)
- pytest (testes automatizados)
- GitHub Actions (IntegraÃ§Ã£o ContÃ­nua)

## Estrutura de pastas

```
DevOps/
â”œâ”€â”€ .github/workflows/   # Pipeline de IntegraÃ§Ã£o ContÃ­nua (GitHub Actions)
â”œâ”€â”€ app/                 # CÃ³digo-fonte da API (Flask)
â”œâ”€â”€ tests/                # Testes automatizados (pytest)
â”œâ”€â”€ docs/                 # DocumentaÃ§Ã£o complementar
â”œâ”€â”€ Dockerfile            # Imagem da aplicaÃ§Ã£o
â”œâ”€â”€ docker-compose.yml    # OrquestraÃ§Ã£o dos containers (app + banco)
â”œâ”€â”€ requirements.txt      # DependÃªncias de produÃ§Ã£o
â”œâ”€â”€ requirements-dev.txt  # DependÃªncias de desenvolvimento/teste
â”œâ”€â”€ README.md
â”œâ”€â”€ CONTRIBUTING.md
â””â”€â”€ LICENSE
```

## Como instalar

1. Clone o repositÃ³rio: `git clone https://github.com/Jessica-NC/DevOps.git`
2. Entre na pasta do projeto: `cd DevOps`
3. Siga as instruÃ§Ãµes da seÃ§Ã£o "Como executar" abaixo.

## Como executar

### Com Docker (recomendado)

```bash
docker compose up --build
```

A API ficarÃ¡ disponÃ­vel em `http://localhost:5000`.

### Localmente, sem Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m app.app
```

## LicenÃ§a

- EvidÃªncia: atualizaÃ§Ã£o da branch features/task-crud para Pull Request.

Este projeto estÃ¡ licenciado sob os termos da licenÃ§a MIT. Veja o arquivo
[LICENSE](LICENSE) para mais detalhes.

- Evidência: atualização da branch features/ci-pipeline para Pull Request.
- Evidência: atualização da branch features/readme-docs para Pull Request.
