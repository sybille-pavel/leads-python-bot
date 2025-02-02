from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    db: str
    user: str
    password: str
    host: str
    port: int

    model_config = SettingsConfigDict(env_file='.env', env_prefix='POSTGRES_', extra='allow')

    def get_sqlalchemy_dsn(self) -> str:
        return f'postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}'


postgres_settings = PostgresSettings()
