import weaviate
from weaviate.connect import ConnectionParams
from src.Core.config import Config

class VectorDb:
    def __init__(self):
        self.client = weaviate.WeaviateClient(
            connection_params=ConnectionParams.from_params(
                http_host=Config.VECTORDB_HOST,
                http_port=Config.VECTORDB_HTTPPORT,
                http_secure=False,
                grpc_host=Config.VECTORDB_HOST,
                grpc_port=Config.VECTORDB_GRCPPORT,
                grpc_secure=False
            )
        )

    def get__weaviate_client(self):
        return self.vectorDatabase
    
