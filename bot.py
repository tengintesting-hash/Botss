import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import select

from handlers import router
from models import Channel, async_session_factory, init_db


async def load_channels() -> list[Channel]:
    async with async_session_factory() as session:
        result = await session.execute(select(Channel))
        return list(result.scalars())


async def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("Задайте змінну середовища BOT_TOKEN.")

    await init_db()

    bot = Bot(token=token)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    channels = await load_channels()
    bot_info = await bot.get_me()

    dp["channels"] = channels
    dp["bot_username"] = bot_info.username

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
