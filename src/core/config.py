from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    admin_ids: str

    model_config = SettingsConfigDict(env_file='.env', extra='allow')

    def get_admin_ids(self):
        return self.admin_ids.split(",")

settings = Settings()
