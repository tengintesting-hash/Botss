import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy import select

from config import settings
from handlers import router
from models import Channel, async_session_factory, init_db


async def load_channels() -> list[Channel]:
    async with async_session_factory() as session:
        result = await session.execute(select(Channel))
        return list(result.scalars())


async def main() -> None:
    if not settings.bot_token:
        raise RuntimeError(
            "Задайте змінну середовища BOT_TOKEN (токен бота з BotFather)."
        )

    await init_db()

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    channels = await load_channels()
    bot_info = await bot.get_me()

    dp["channels"] = channels
    web_app_url = settings.web_app_url or f"https://t.me/{bot_info.username}/app"
    dp["web_app_url"] = web_app_url

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
