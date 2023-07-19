import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher
import asyncio
from keyboards.ui_commands import set_bot_commands

from handlers import handler
load_dotenv()

# Включаем логирование, чтобы не пропустить важные сообщения
# Объект бота
token = os.getenv('TOKEN')

async def main() -> None:

    # Dispatcher is a root router
    dp = Dispatcher()
    # ... and all other routers should be attached to Dispatcher
    dp.include_routers(handler.router)

    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(token, parse_mode="HTML")
    # And the run events dispatching
    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(filename='logs.log', format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S', level=logging.INFO)
    asyncio.run(main())
