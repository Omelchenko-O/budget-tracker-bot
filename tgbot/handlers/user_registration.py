from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from infrastructure.database.repo.requests import RequestsRepo
from tgbot.misc.states import Registration

user_registration_router = Router()


@user_registration_router.message(Command('registration'))
async def user_registration_name(message: Message, state: FSMContext):
    await message.answer('Реєстрація не займе багато часу, лише два питання.')
    await message.answer('1/2. Напишіть своє імʼя:')

    await state.set_state(Registration.ask_city)


@user_registration_router.message(Registration.ask_city)
async def user_registration_city(message: Message, state: FSMContext):
    await state.update_data(name=message.text, telegram_id=message.from_user.id)
    await message.answer('В якому місті ви живете?')

    await state.set_state(Registration.complete)


@user_registration_router.message(Registration.complete)
async def user_registration_complete(message: Message, state: FSMContext, repo: RequestsRepo):
    await state.update_data(city=message.text)

    user_data = await state.get_data()
    await message.answer(f'Дякую, реєстрацію завершено!\nПриємно познайомитись, <b>{user_data["name"]}</b>')

    # TODO add user to DB
    await repo.users.create_user(
        telegram_id=user_data['telegram_id'],
        username=user_data['name'],
        city=user_data['city']
    )
    await message.answer('added to db!')
    await state.clear()
