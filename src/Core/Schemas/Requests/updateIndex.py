from pydantic import BaseModel, field_validator, Field, ValidationInfo
from src.Core.Enums import VectoreDataBaseNames

class UpdateIndex(BaseModel):

    # Campo referente ao Nome do Index
    index_name: str

    chunk_size: int = Field(default=1024, gt=1024)

    chunk_overlap : int = Field(default=24, gt=1)

    reader_type: str 
    


    # Função/Anotação para criar uma validação específica
    @field_validator("index_name")
    def index_validator(cls, v):
        if v not in [ VectoreDataBaseNames.LEGISLACAO , VectoreDataBaseNames.JURISPRUDENCIA, VectoreDataBaseNames.CONTRATOSENVIADOS, VectoreDataBaseNames.CLAUSULASMODELOS, VectoreDataBaseNames.ANALISESDERISCO]:
            raise ValueError("index name not allowed.")
        return v
    
     # Função/Anotação para validar o tipo de reader
    @field_validator("reader_type")
    def index_validator(cls, v):
        if v not in ["files", "web"]:
            raise ValueError("index name not allowed.")
        return v
    

    # Validação para garantir que chunk_size seja maior que chunk_overlap
    @field_validator("chunk_size")
    def validator_size_greater_overlap(cls, v, values: ValidationInfo):
        if "chunk_overlap" in values.data and v <= values.data['chunk_overlap']:
            raise ValueError("Chunck Size must be greater than chunck overlap")
        return v
    