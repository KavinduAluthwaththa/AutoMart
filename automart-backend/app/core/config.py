from pydantic import BaseSettings


class Settings(BaseSettings):
            PROJECT_NAME: str = "AutoMart"
            SQLALCHEMY_DATABASE_URL: str = "postgresql+psycopg2://user:pass@localhost/automart"
            SECRET_KEY: str = "change-me"
            ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24


class Config:
    env_file = ".env"

settings = Settings()