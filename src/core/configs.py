from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://user:admin@localhost:5432/faculdade'
    DBBaseModel: ClassVar = declarative_base()

    JWT_SECRET: str = 'Ub3sifkbu_k7HUDIeYDlxteoyL8HzhslKpkN698hYc8'
    '''
    para fazer no python repl:
    import secrets
    token: str = secrets.token_urlsafe(32)
    '''
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7

    class Config:
        case_sensitive: True

settings: Settings = Settings()