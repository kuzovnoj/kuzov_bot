from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


# Создаём кнопки с ответами
button_get = InlineKeyboardButton(
    text=LEXICON_RU["get_button"],
    callback_data="GET"
    )
button_retrieve = InlineKeyboardButton(
    text=LEXICON_RU["retrieve_button"],
    callback_data='retrieve'
    )

# Создаём клавиатуру с кнопками
keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[[button_get], [button_retrieve]]
)