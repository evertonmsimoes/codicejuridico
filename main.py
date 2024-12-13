import uvicorn

from src.Core.config import config

if __name__ == "__main__":
    uvicorn.run(
        app='src.Core.server:app',
        reload=True if config.ENVIRONMENT != "production" else False, # Configurando o Hot Reload de forma automatica em ambientes que não são de produção.
        workers=1, # Aqui Definimos o Número de workers lidando com nossas Requisições.
    )