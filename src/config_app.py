from dotenv import load_dotenv
import os

load_dotenv()
from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    SQLALCHEMY_DATABASE_URL: str

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expires_s: int = 3600


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)

