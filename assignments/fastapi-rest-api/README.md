# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciamento de tarefas usando FastAPI. Você praticará rotas HTTP, validação de dados com modelos Pydantic e operações CRUD.

## 📝 Tarefas

### 🛠️ Implemente as rotas de consulta

#### Descrição
Use o starter code para iniciar a aplicação, instalar as dependências e explorar a documentação interativa do FastAPI. Salve uma cópia de `starter-code.py` como `main.py` antes de executar os comandos abaixo.

```bash
python -m pip install fastapi uvicorn
uvicorn main:app --reload
```

A documentação interativa estará disponível em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Iniciar sem erros com Uvicorn e exibir a documentação interativa em `/docs`.
- Implementar `GET /tasks` para retornar todas as tarefas.
- Implementar `GET /tasks/{task_id}` para retornar uma tarefa pelo ID ou responder com status 404 quando ela não existir.

### 🛠️ Adicione tarefas com validação

#### Descrição
Implemente a criação de tarefas. Use um modelo Pydantic para validar os dados enviados pelo cliente e gere um ID para cada nova tarefa.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` com os campos `title`, `description` e `completed`.
- Validar automaticamente o corpo da requisição usando o modelo Pydantic fornecido.
- Atribuir um ID único à nova tarefa e incluí-la na resposta.
- Responder com status 201 quando uma tarefa for criada.

### 🛠️ Atualize e remova tarefas

#### Descrição
Complete as operações de atualização e remoção, usando o ID da tarefa no caminho da rota e tratando IDs inexistentes.

#### Requisitos
O programa concluído deve:

- Implementar `PATCH /tasks/{task_id}` para atualizar somente os campos enviados na requisição.
- Implementar `DELETE /tasks/{task_id}` para remover a tarefa solicitada.
- Responder com status 404 para operações sobre IDs que não existem.
- Permitir conferir as operações e respostas pela documentação interativa em `/docs`.
