from core.postgres_settings import postgres_settings
from tortoise import Tortoise

# Подключение к БД
async def init_db():
    db_url = postgres_settings.get_sqlalchemy_dsn()

    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["models.lead"]}
    )
    await Tortoise.generate_schemas()