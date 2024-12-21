import weaviate
from src.Core.config import Config

class VectorDb:
    def __init__(self):
        self.vectorDatabase = weaviate.Client(url=Config.DATABASE)

    def get__weaviate_client(self):
        return self.vectorDatabase
    
