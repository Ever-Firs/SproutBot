import asyncio
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import text
from keyboards import start_kb

router = Router()
text = text.Text()


@router.message((F.text.lower() == 'назад') | (F.text.lower() == '/start') | (F.text.lower() == 'start'))
async def start_message(message: Message):
    await message.answer(text.start, reply_markup=start_kb.start_kb)


@router.message((F.text.lower() == 'о нас') | (F.text.lower() == 'наши проекты') | (F.text.lower() == 'где мы') | (F.text.lower() == 'помощь'))
async def link(message: Message):
    msg = message.text.lower()

    if msg == 'о нас':
        await message.answer(text.me, reply_markup=start_kb.kb_close)
    if msg == 'наши проекты':
        await message.answer(text.project, reply_markup=start_kb.kb_project)
    if msg == 'где мы':
        await message.answer(text.link, reply_markup=start_kb.kb_link)
    if msg == 'помощь':
        await message.answer(text.help, reply_markup=start_kb.kb_close)
