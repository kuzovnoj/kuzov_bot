from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import keyboard1
from lexicon.lexicon import LEXICON_RU
from services.services import get_request, retrieve_request

user_router = Router()


# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=keyboard1)


# Этот хэндлер срабатывает на команду /help
@user_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"])


# Этот хэндлер срабатывает на 
@user_router.callback_query(F.data == LEXICON_RU["get_button"])
async def process_get(callback: CallbackQuery):
    result = get_request()
    for res in result['results']:
        await callback.message.answer(text=str(res))


@user_router.callback_query(F.data == LEXICON_RU["retrieve_button"])
async def process_retrieve(callback: CallbackQuery):
    result = retrieve_request()
    await callback.message.answer(text=str(result))