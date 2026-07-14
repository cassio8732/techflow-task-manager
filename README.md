# TechFlow Task Manager

## Objetivo do Projeto
Este projeto simula o desenvolvimento de um sistema de gerenciamento de
tarefas para a **TechFlow Solutions**, contratada por uma startup de
logística fictícia. O objetivo é permitir o acompanhamento do fluxo de
trabalho em tempo real, a priorização de tarefas críticas e o
monitoramento do desempenho da equipe, aplicando conceitos de
Engenharia de Software e metodologias ágeis.

## Escopo Inicial
O sistema deve permitir, no mínimo:
- Criar tarefas
- Listar tarefas
- Atualizar o status de uma tarefa (A Fazer / Em Progresso / Concluído)
- Remover tarefas

Além da API, o projeto conta com uma **interface visual em HTML**, que
consome essa API e exibe as tarefas organizadas em um quadro no estilo
Kanban (A Fazer / Em Progresso / Concluído), facilitando a demonstração
do CRUD funcionando na prática.

## Metodologia Ágil Adotada
O projeto foi organizado utilizando **Kanban**, por ser uma metodologia
simples de visualizar o fluxo de trabalho e adequada ao tamanho da
equipe (neste caso, um único desenvolvedor simulando o papel de
dev + gestor de projeto). O quadro foi criado na aba **Projects** do
GitHub, com as colunas **A Fazer**, **Em Progresso** e **Concluído** —
o mesmo padrão refletido na interface visual do sistema.

## Estrutura do Repositório
/src
app.py              → código-fonte da API Flask
templates/
index.html        → interface visual do CRUD (consome a API)
/tests                → testes automatizados (Pytest)
/docs                 → diagramas e prints usados na documentação
.github/workflows     → pipeline de integração contínua (GitHub Actions)

## Como Executar o Sistema
1. Clone o repositório
2. Instale as dependências:
pip install -r requirements.txt
3. Entre na pasta `src` e rode a aplicação:
cd src
python app.py
4. Acesse `http://127.0.0.1:5000/` no navegador para ver a interface
   visual do sistema, com o quadro de tarefas e o formulário de criação.

   A API também está disponível diretamente através dos seguintes
   endpoints:
   - `GET /tasks` — lista todas as tarefas
   - `POST /tasks` — cria uma tarefa (`{"title": "..."}`)
   - `PUT /tasks/<id>` — atualiza uma tarefa
   - `DELETE /tasks/<id>` — remove uma tarefa

## Como Rodar os Testes
pytest tests/ -v
Os testes também são executados automaticamente a cada `push` através
do pipeline configurado em `.github/workflows/tests.yml`.

## Gestão de Mudanças — Alteração de Escopo
Durante o desenvolvimento, identificou-se que o cliente (startup de
logística) precisava **priorizar tarefas críticas**, conforme descrito
no desafio original. Por esse motivo, foi adicionado um novo campo,
**`priority`** (prioridade: alta / média / baixa), ao modelo de tarefa,
que inicialmente não fazia parte do escopo.

Essa mudança foi registrada:
- Como um novo card no quadro Kanban ("Adicionar campo de prioridade")
- Através de um commit específico implementando a alteração
- Nesta seção do README, como justificativa da mudança

Essa alteração exemplifica como metodologias ágeis permitem incorporar
mudanças de escopo de forma controlada, sem comprometer as entregas já
realizadas.

## Testes Automatizados
Foram implementados testes unitários cobrindo os principais fluxos do
CRUD: criação (com e sem validação), listagem, atualização e remoção
de tarefas. Isso garante que alterações futuras no código não quebrem
funcionalidades já existentes, seguindo os princípios de controle de
qualidade contínuo.