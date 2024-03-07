from fastapi import FastAPI
from tortoise import Tortoise
from app.api.endpoints import events
from dotenv import load_dotenv
from app.db.database import TORTOISE_ORM
from tortoise.contrib.fastapi import register_tortoise

load_dotenv()

app = FastAPI()

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

Tortoise.init_models(["app.models"], "app")

app.include_router(events.router)
