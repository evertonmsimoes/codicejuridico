from enum import Enum
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Carregando variaveis do arquivo .env

load_dotenv(".env")

# Enum para Definirmos os tipo de ambientes.
class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"

# Classe do pydantic para lidarmos com o carregamento de variáveis de ambiente.
class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


# cCarre
class Config(BaseConfig):
    DEBUG: int = int(os.getenv("DEBUG", 0)) # Aqui desativamos ou Ativamos os Logs Detalhados.
    ENVIRONMENT: EnvironmentType = EnvironmentType(os.getenv("ENVIRONMENT", "development")) # Aqui Definimos o tipo de Ambiente que estamos trabalhando.
    API_KEY: str = str(os.getenv("API_KEY"))

# Função para validar se o ENVIRONMENT esté dentro dos Valores definidos.
def validate_environment(config: Config):
    if config.ENVIRONMENT.value not in EnvironmentType.__members__.values():
        raise ValueError(f"ENVIRONMENT '{config.ENVIRONMENT.value}' não é válido. Use um dos seguintes valores: {', '.join(EnvironmentType.__members__.values())}")

try:
    # Carregando as configurações.
    config: Config = Config()
    # Validando o Ambiente.
    validate_environment(config=config)
except ValueError as Err:
    print("Erro de Validação: ", Err)