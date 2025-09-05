import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv

from bot.handlers import router
from bot.middleware import AuthMiddleware

load_dotenv(os.path.join("..", ".env"))


# Объект бота
token = os.getenv("BOT_TOKEN")
bot = Bot(
    token=token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
        )
    )

redis_url = os.getenv("REDIS_URL")
storage = RedisStorage.from_url(redis_url)

# Диспетчер
dp = Dispatcher(storage=storage)

dp.include_routers(router)
dp.message.middleware(AuthMiddleware())
dp.callback_query.outer_middleware(AuthMiddleware())


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

