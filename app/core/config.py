
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    #URL e a senha do banco de dados
    DATABASE_URL: str
    SECRET_KEY: str

    #configuração que acessa as variaveis do arquivo .env
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()