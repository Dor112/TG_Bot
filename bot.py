import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from wheather import get_wheather


scheduler = AsyncIOScheduler()
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("wheather"))
async def cmd_wheather(message: types.Message):
    wheather_data = await get_wheather()
    await message.reply(wheather_data)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

