from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from keyboards import keyboard

from aiogram import Bot, Router, types
from aiogram.filters import Command, Text
from aiogram.types import Message, InlineKeyboardMarkup
import logging


from handlers import utilits

router = Router()
logger = logging.getLogger(__name__)
logging.basicConfig(filename='logs.log',
                    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                    datefmt='%H:%M:%S', level=logging.INFO)
# Определение состояния для запроса текста
class TextSearchForm(StatesGroup):
    waiting_for_book_name = State()
    waiting_propose_book = State()


@router.message(Command(commands=["admin"]))
async def admin_command(message: Message):
    username = message.from_user.username
    username = "".join(["@", username])
    await message.answer(text="Выбери действие из меню.")


@router.message(Command(commands=["start"]))
async def start_command(message: Message):
    # keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    userFirstname = message.from_user.first_name
    username = message.from_user.username
    username = "".join(["@", username])
    # username = "123"

    await message.answer(f"Привет, {userFirstname}, добро пожаловать в библиотеку! Выбери действие из меню.")
