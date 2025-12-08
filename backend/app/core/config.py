from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CodeSeer"
    API_V1: str = "/api/v1"

    class Config:
        env_file = ".env"

settings = Settings()
