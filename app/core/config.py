from pydantic_settings import BaseSettings
#Base Settings is a special class in pydantic which automatically reads
# all the enviromental variable credentials

class Settings(BaseSettings):
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    DATABASE_URL: str
    REDIS_URL: str

    class Config: # This config class tells the pydantic from which class it will read credentials
        env_file = ".env"

settings=Settings()

