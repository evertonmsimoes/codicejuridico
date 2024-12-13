from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


# Função para Adicionar as Rotas da Nossa Aplicação;
def init_routers(app_: FastAPI) -> None:
#    app_.include_router()
    pass

# Função para configurar os middlewares de nossa aplicação, em nosso cenario usamos apenas para configurar o recursos de CORS.
def make_middleware() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    ]

    return middleware


# Função para instaciar a nossa instancia do Fast API.
def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Códice Jurídico",
        description="An Example of AI Application by Everton Simões.",
        version="1.0.0",
        middleware=make_middleware(),
    )

    init_routers(app_=app_)
    return app_

app: FastAPI = create_app()