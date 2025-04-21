from llama_index.embeddings.gemini import GeminiEmbedding
from src.Core import Config

class GeminiEmbedder:
    
    def __init__(self):
        self.emmberder = GeminiEmbedding(
            api_key=Config.API_KEY
        )
    
    def getGeminiEmbedder(self, model: str) -> GeminiEmbedding:
        self.emmberder.modedel_name= model
        return self.emmberder
