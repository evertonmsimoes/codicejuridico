from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

from src.Core.config import Config

from src.Core.Dependencies.logging import Logging


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


# Incluindo Logger
def init_logger(app_: FastAPI) -> None:
    logger = Logging()
    logger.add_logging(app_=app_)


# Função para instaciar a nossa instancia do Fast API.
def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Códice Jurídico",
        description="An Example of AI Application by Everton Simões.",
        version="1.0.0",
        docs_url=None if Config.ENVIRONMENT == "production" else "/docs", # Definindo configurações do Swagger UI, para que a documentação seja visível apenas em ambientes de teste.
        redoc_url=None if Config.ENVIRONMENT == "production" else "/rdoc",
        middleware=make_middleware(), # Configurando os Middlewares
    )

    init_routers(app_=app_) # Adicionando as Rotas a aplicação

    init_logger(app_=app_) # Inicializar o logger
    return app_

app: FastAPI = create_app()

