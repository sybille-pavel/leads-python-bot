from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    bot_token: str

    model_config = SettingsConfigDict(env_file='.env', extra='allow')


bot_settings = BotSettings()
