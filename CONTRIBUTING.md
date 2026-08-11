# Guia de Contribuição

Este documento descreve o fluxo de trabalho colaborativo adotado pela
CodeFactory Solutions após a implantação da Cultura DevOps.

## Estratégia de branches

- `main` — código estável, correspondente ao que está em produção. Só recebe
  merges vindos de `desenvolvimento`.
- `desenvolvimento` — branch de integração. Reúne as features já concluídas
  e testadas antes de irem para `main`.
- `features/<nome-da-feature>` — uma branch por funcionalidade ou tarefa,
  criada a partir de `desenvolvimento` e finalizada via Pull Request.

## Fluxo de trabalho

1. Criar uma branch a partir de `desenvolvimento`:
   `git checkout desenvolvimento && git checkout -b features/minha-feature`
2. Commitar em pequenos incrementos, com mensagens no padrão
   [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`,
   `fix:`, `docs:`, `test:`, `chore:`, `ci:`).
3. Enviar a branch (`git push origin features/minha-feature`) e abrir um
   Pull Request para `desenvolvimento`.
4. Pelo menos um outro integrante revisa e aprova o PR antes do merge.
5. Periodicamente, `desenvolvimento` é mesclada em `main` via Pull Request,
   marcando uma nova versão estável do projeto.

## Padrão de commits

Utilizamos mensagens curtas, no imperativo, prefixadas pelo tipo da
alteração, por exemplo:

- `feat: adiciona endpoint de atualização de tarefas`
- `fix: corrige validacao do campo title`
- `docs: atualiza instrucoes de instalacao`

## Issues, labels e milestones

Toda nova funcionalidade ou correção deve estar associada a uma *Issue* no
GitHub, categorizada com as *labels* apropriadas (`feature`, `bug`,
`documentation`, `devops`) e vinculada a um *Milestone* da entrega em
andamento. O quadro do *Projects* é utilizado para acompanhar o status
(`A fazer`, `Em andamento`, `Em revisão`, `Concluído`) de cada item.
