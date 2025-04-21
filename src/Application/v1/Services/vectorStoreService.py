from src.Core.Database import VectorDataBase
from src.Core.Schemas.Requests import UpdateIndex

from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.weaviate import WeaviateVectorStore
from llama_index.core.node_parser import SentenceSplitter


class VectorStoreService:
    def __init__(self):
        self.vectorDataBase = VectorDataBase().get__weaviate_client()

    def create_index(self, data: UpdateIndex) -> None:
        
        self.vectorDataBase.connect()

        vector_store = WeaviateVectorStore(
            weaviate_client=self.vectorDataBase,
            index_name=data.index_name
        )

        splitter = SentenceSplitter(chunk_size=data.chunk_size)

        documecnts = []


        try:
            VectorStoreIndex.from_documents(
                documents=documecnts, 
                transformations=[splitter], 
                storage_context=storage_context, 
                embed_model=embed_model
            )
        except:
            pass
    
        pass
    

    