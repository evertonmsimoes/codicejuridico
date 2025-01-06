from src.Core.Database import VectorDataBase

class VectorStoreService:
    def __init__(self):
        self.vectorDataBase = VectorDataBase().get__weaviate_client()

    
    

    