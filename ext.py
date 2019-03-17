from tortoise import Tortoise

from config import DB_URL

async def init_db(create_db=False):
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['models']},
    )