from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="О нас"),
            KeyboardButton(text="Наши проекты")
        ],
        [
            KeyboardButton(text="Где мы"),
            KeyboardButton(text="Помощь")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Что хочешь узнать?',
    selective=True
)

kb_close = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Вернуться назад',
    selective=True
)

kb_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Discord', url='https://discord.gg/wyN4EHEH'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=Sprout_Channel')
        ]
    ]
)

kb_project = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sprout', url='http://sproutt.ru'),
        ]
    ]
)