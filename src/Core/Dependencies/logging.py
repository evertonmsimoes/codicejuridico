import logging
from fastapi import FastAPI, Request
from time import time

class Logging:

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        self.logger = logging.getLogger("Códice Jurídico")

    def add_logging(self, app_: FastAPI) -> None:
        @app_.middleware("http") # Assinatura que permite filtrar que permite filtrar as requisições HTTP que entram em uma Aplicação;
        async def log_request(request: Request, call_next):
            start_time = time()
            response = await call_next(request)

            process_time = time() - start_time
            
            self.logger.info(
                 f"Request: {request.method} {request.url.path} | "
                 f"Status: {response.status_code} | "
                 f"Process Time: {process_time:.2f}s"
            )
            
            return response