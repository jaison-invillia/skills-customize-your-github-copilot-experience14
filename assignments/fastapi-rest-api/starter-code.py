"""
FastAPI REST API - Starter Code
Tarefa: Construindo APIs REST com FastAPI

Este é o código inicial para você começar. Siga as instruções no README.md
para implementar os endpoints e funcionalidades necessárias.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

# TODO: Inicialize o aplicativo FastAPI
app = FastAPI(
    title="Task Manager API",
    description="Uma API REST simples para gerenciar tarefas",
    version="1.0.0"
)

# TODO: Defina o modelo Pydantic para uma Tarefa
class Task(BaseModel):
    """
    Modelo de dados para uma tarefa.
    Complete este modelo com os campos necessários.
    """
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=100, description="Título da tarefa")
    description: Optional[str] = Field(None, max_length=500, description="Descrição detalhada da tarefa")
    completed: bool = Field(False, description="Status de conclusão da tarefa")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Estudar FastAPI",
                "description": "Completar a tarefa de programação sobre FastAPI",
                "completed": False
            }
        }


# Armazenamento em memória para as tarefas
tasks_db: List[Task] = []
task_id_counter = 1


# TODO: Tarefa 1 - Criar endpoint de boas-vindas
@app.get("/")
def read_root():
    """
    Endpoint de boas-vindas.
    Retorna uma mensagem simples.
    """
    # Implemente este endpoint
    pass


# TODO: Tarefa 2 - Implementar endpoints CRUD

@app.post("/tasks/", status_code=201, tags=["Tasks"])
def create_task(task: Task):
    """
    Cria uma nova tarefa.
    """
    # Implemente este endpoint
    pass


@app.get("/tasks/", tags=["Tasks"])
def get_all_tasks():
    """
    Retorna todas as tarefas.
    """
    # Implemente este endpoint
    pass


@app.get("/tasks/{task_id}", tags=["Tasks"])
def get_task(task_id: int):
    """
    Retorna uma tarefa específica pelo ID.
    """
    # Implemente este endpoint
    pass


@app.put("/tasks/{task_id}", tags=["Tasks"])
def update_task(task_id: int, task: Task):
    """
    Atualiza uma tarefa existente.
    """
    # Implemente este endpoint
    pass


@app.delete("/tasks/{task_id}", status_code=204, tags=["Tasks"])
def delete_task(task_id: int):
    """
    Deleta uma tarefa.
    """
    # Implemente este endpoint
    pass


# Para executar o servidor, use o comando:
# uvicorn starter-code:app --reload
#
# Depois acesse:
# - API: http://localhost:8000
# - Documentação interativa: http://localhost:8000/docs
# - Documentação alternativa: http://localhost:8000/redoc
