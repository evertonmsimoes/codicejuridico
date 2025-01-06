from pydantic import BaseModel, field_validator, Field


class UpdateIndex(BaseModel):

    # Campo referente ao Nome do Index
    index_name: str

    chunk_size: int = Field(default=1024, gt=1024)

    chunk_overlap : int = Field(default=24, gt=1)

  


    # Função/Anotação para criar uma validação específica
    @field_validator("index_name")
    def index_validator(cls, v):
        if v not in ["Legislacao", "Jurisprudencia", "ClausulasModelos", "AnalisesDeRisco", "ContratosEnviados"]:
            raise ValueError("index name not allowed.")
        return v
    

    @field_validator("chunk_size")
    def validator_size_greater_overlap(cls, v, value):
        if v <= value['chunk_overlap']:
            raise ValueError("Chunck Size must be greater than chunck overlap")
        return v