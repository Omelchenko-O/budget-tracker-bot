from aiogram import types, Router, F
from aiogram.filters import StateFilter
from aiogram.utils.markdown import hcode

echo_router = Router()


@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: types.Message, repo):
    if message.text.upper() == 'ID':
        await message.answer(f'Ваш telegram ID: {hcode(message.from_user.id)}')
        repo.pr()
    else:
        text = [
            "Ехо без стану.",
            "Повідомлення:",
            message.text
        ]

        await message.answer('\n'.join(text))
