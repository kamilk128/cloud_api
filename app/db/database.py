from os import getenv
from dotenv import load_dotenv

load_dotenv()

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": str(getenv("DB_HOST")),
                "port": str(getenv("DB_PORT")),
                "user": str(getenv("DB_USER")),
                "password": str(getenv("DB_PASSWORD")),
                "database": str(getenv("DB_NAME")),
            },
        },
    },
    "apps": {
        "app": {
            "models": ["app.models", "aerich.models"],
        },
    },
}
