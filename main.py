import asyncio
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv, find_dotenv
from handlers import message

load_dotenv(find_dotenv())

#python main.py

async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher(bot=bot)

    dp.include_routers(message.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
