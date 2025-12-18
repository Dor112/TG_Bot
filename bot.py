import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
from wheather import get_wheather
from aiogram.fsm.storage.memory import MemoryStorage
#from Database_con import db_connection
from Database_con import cur

scheduler = AsyncIOScheduler()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
#conn = db_connection()
cur.execute("SELECT id FROM users")
auto_users = [row[0] for row in cur]
#print(auto_users)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")

@dp.message(Command("wheather"))
async def cmd_wheather(message: types.Message):
    wheather_data = await get_wheather()
    await message.reply(wheather_data)

@dp.message(Command("auto_on"))
async def cmd_auto_on(message: types.Message):
    user_id = message.from_user.id
    user_id = int(user_id)
    if user_id in auto_users:
        await message.answer("Автоотправка уже работает!")
    else:
        cur.execute("INSERT INTO users (id) VALUES (%s)", (user_id,))
        auto_users.append(user_id)
        await message.answer("Вы были добавленны в список!")

        wheather_data = await get_wheather()
        await message.reply(wheather_data)

@dp.message(Command("auto_off"))
async def cmd_auto_off(message: types.Message):
    user_id = message.from_user.id
    if user_id in auto_users:
        auto_users.remove(user_id)
        await message.answer("Автоотправка выключена.")
    else:
        await message.answer("Автоотправка не была включена.")

async def send_to_subs():
    if not auto_users:
        return 0
    weather_data = await get_wheather()
    for user_id in list(auto_users):
        await bot.send_message(user_id,weather_data)
async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_to_subs, "interval", seconds = 5)
    scheduler.start()
    try:
        await dp.start_polling(bot)
    finally:
        scheduler.shutdown()


if __name__ == "__main__":
    asyncio.run(main())