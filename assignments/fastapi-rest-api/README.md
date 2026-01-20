# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir uma API REST funcional usando o framework FastAPI. Você criará endpoints para gerenciar uma lista de tarefas (to-do list), implementando operações CRUD (Create, Read, Update, Delete) e explorando conceitos essenciais de desenvolvimento de APIs.

## 📝 Tasks

### 🛠️	Criar Servidor FastAPI Básico

#### Description
Crie um servidor FastAPI básico com um endpoint de boas-vindas. Configure a estrutura inicial do projeto e verifique se o servidor está funcionando corretamente.

#### Requirements
Completed program should:

- Importar e inicializar o FastAPI
- Criar um endpoint GET na rota raiz ("/") que retorna uma mensagem de boas-vindas
- Executar o servidor usando uvicorn
- Retornar um JSON com uma mensagem de boas-vindas quando acessado


### 🛠️	Implementar Endpoints CRUD para Tarefas

#### Description
Implemente um sistema completo de gerenciamento de tarefas com operações CRUD. Crie endpoints para criar, listar, atualizar e deletar tarefas usando métodos HTTP apropriados.

#### Requirements
Completed program should:

- Criar um modelo Pydantic para representar uma tarefa (com id, título, descrição e status)
- Implementar endpoint POST `/tasks/` para criar novas tarefas
- Implementar endpoint GET `/tasks/` para listar todas as tarefas
- Implementar endpoint GET `/tasks/{task_id}` para buscar uma tarefa específica
- Implementar endpoint PUT `/tasks/{task_id}` para atualizar uma tarefa existente
- Implementar endpoint DELETE `/tasks/{task_id}` para deletar uma tarefa
- Armazenar as tarefas em uma lista em memória
- Retornar códigos de status HTTP apropriados (200, 201, 404, etc.)


### 🛠️	Adicionar Validação e Documentação

#### Description
Melhore sua API adicionando validação de dados usando Pydantic e explore a documentação automática gerada pelo FastAPI. Adicione tratamento de erros apropriado.

#### Requirements
Completed program should:

- Adicionar validações no modelo Pydantic (ex: título não pode ser vazio, comprimento mínimo/máximo)
- Implementar tratamento de erro quando uma tarefa não for encontrada (HTTPException)
- Adicionar descrições e exemplos aos modelos usando Field do Pydantic
- Testar a API usando a documentação interativa do Swagger UI (`/docs`)
- Adicionar tags aos endpoints para organizar a documentação
- Incluir responses personalizadas nos decoradores dos endpoints
