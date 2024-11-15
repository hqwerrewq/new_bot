import random

from aiogram import Bot
from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

from src.pyrogram import members
from src.utils.prime_activity import get_prime_activity
from src.filters import filters

router = Router()


@router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer(f'Привет, {msg.from_user.username}.')


@router.message(F.text.lower().contains('визард'))
async def help_handler(msg: Message):
    await msg.answer(f'Аве, Визард...')


@router.message(F.text.lower().contains('аве'))
async def help_handler(msg: Message):
    await msg.answer(f'Хуй соси...')

@router.message(Command('mumble'))
async def get_mumble_handler(msg: Message, bot: Bot):
    if await filters.member_filter(msg, bot) is True:
        await msg.answer(text=f'\n'
                              f'*___Mumble___*:\n'
                              f'Адрес: `s1.mumble-voip.ru`\n'
                              f'Порт: `2540`\n'
                              f'Пароль: `None`', parse_mode='Markdown')


@router.message(Command('buff'))
async def get_mumble_handler(msg: Message, bot: Bot):
    if await filters.member_filter(msg, bot) is True:
        await msg.answer(text=f'\n'
                              f'*Бафф Мага*:\n'
                              f'Схема: `XYZ45-PIZDA`\n'
                              f'*Бафф Воина*:\n'
                              f'Схема: `None`', parse_mode='Markdown')


@router.message(F.text == "Моль")
async def tag_all_handler(msg: types.Message, bot: Bot):
    if await filters.admins_filter(msg, bot) is True:
        chat_id = msg.chat.id
        participant_name = await members.pyro_get_chat_members(chat_id)
        for i in range(0, len(participant_name), 100):
            mentions = ''.join(f'@{str(m)} ' for m in participant_name[i:i + 100])
            msg_text = f"Моль, {mentions}"
            await bot.send_message(chat_id=chat_id, text=msg_text)


@router.message(Command('prime'))
async def prime_handler(msg: Message):
    await msg.answer(f'Еблан? Сказано же, не работает...')
