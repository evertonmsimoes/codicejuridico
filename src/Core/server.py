from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware


def init_routers(app_: FastAPI) -> None:
    app_.include_router()


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