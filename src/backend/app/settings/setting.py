from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_HOST: str = Field(default='db', validation_alias='POSTGRES_HOST')
    POSTGRES_USER: str = Field(default=..., validation_alias='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field(default=..., validation_alias='POSTGRES_PASSWORD')
    POSTGRES_DB: str = Field(default=..., validation_alias='POSTGRES_DB')

    @property
    def async_database_url(self) -> str:
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}/{self.POSTGRES_DB}'


settings = Settings()
