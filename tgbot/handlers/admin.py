from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tgbot.config import Config
from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply("Вітаю, адміне!")


@admin_router.message(Command('admin'))
async def create_tables(message: Message, config: Config):
    await message.answer(config.db.construct_sqlalchemy_url())
