# CodeFactory TaskManager

![CI](https://github.com/Jessica-NC/DevOps/actions/workflows/ci.yml/badge.svg)

> Projeto demonstrativo desenvolvido como parte da adoção da Cultura DevOps na
> CodeFactory Solutions (Atividade Prática — DevOps e Integração Contínua, UNINTER).

## Descrição do projeto

O **CodeFactory TaskManager** é uma API REST simples de gerenciamento de
tarefas, utilizada como projeto de referência para demonstrar, na prática,
a adoção da Cultura DevOps pela equipe da CodeFactory Solutions:
versionamento com Git/GitHub, containerização com Docker e um pipeline de
Integração Contínua.

## Objetivo

Demonstrar como práticas e ferramentas de DevOps (controle de versão
colaborativo, containers e automação de build/testes) podem resolver os
problemas de padronização, integração e agilidade enfrentados pela equipe
de desenvolvimento da CodeFactory Solutions.

## Tecnologias utilizadas

- Python 3.12 + Flask (API REST)
- Flask-SQLAlchemy (ORM)
- PostgreSQL (banco de dados em produção/Docker)
- SQLite (banco em memória para testes)
- Docker e Docker Compose (containerização)
- pytest (testes automatizados)
- GitHub Actions (Integração Contínua)

## Estrutura de pastas

```
DevOps/
├── .github/workflows/   # Pipeline de Integração Contínua (GitHub Actions)
├── app/                 # Código-fonte da API (Flask)
├── tests/                # Testes automatizados (pytest)
├── docs/                 # Documentação complementar
├── Dockerfile            # Imagem da aplicação
├── docker-compose.yml    # Orquestração dos containers (app + banco)
├── requirements.txt      # Dependências de produção
├── requirements-dev.txt  # Dependências de desenvolvimento/teste
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Como instalar

1. Clone o repositório: `git clone https://github.com/Jessica-NC/DevOps.git`
2. Entre na pasta do projeto: `cd DevOps`
3. Siga as instruções da seção "Como executar" abaixo.

## Como executar

### Com Docker (recomendado)

```bash
docker compose up --build
```

A API ficará disponível em `http://localhost:5000`.

### Localmente, sem Docker

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python -m app.app
```

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo
[LICENSE](LICENSE) para mais detalhes.

- Evid�ncia: atualiza��o da branch features/ci-pipeline para Pull Request.
