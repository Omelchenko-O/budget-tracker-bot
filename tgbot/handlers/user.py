from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from magic_filter import F

from tgbot.keyboards.callback_datas import ProfileCallbackFactory
from tgbot.keyboards.inline import profile_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Вітаю, звичайний користувач!")


@user_router.message(Command('profile'))
async def profile(message: Message):
    # TODO get user info from DB
    text = [
        'Вітаю! Ваш профіль:',
        f'Імʼя: {None}',
        f'Місто: {None}',
        f'Дата реєстрації: {None}',
        f'Дата останнього оновлення профілю: {None}'
    ]

    await message.answer('\n'.join(text), reply_markup=profile_keyboard())


@user_router.callback_query(ProfileCallbackFactory.filter(F.action == 'edit'))
async def profile_callback(call: CallbackQuery, callback_data: ProfileCallbackFactory):
    await call.message.edit_text('Що саме ви хоете змінити?', reply_markup=profile_keyboard())

    await call.answer()


@user_router.callback_query(ProfileCallbackFactory.filter())
async def profile_callback(call: CallbackQuery, callback_data: ProfileCallbackFactory):
    if callback_data.action == 'edit':
        await call.message.answer(call.data)
    elif callback_data.action == 'delete':
        await call.message.answer(call.data)

    await call.answer()
