from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.keyboards.callback_datas import TrackerCallbackFactory, ProfileCallbackFactory


def budget_tracker_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='Add expense', callback_data=TrackerCallbackFactory(action='expense'))
    builder.button(text='Add income', callback_data=TrackerCallbackFactory(action='income'))

    builder.adjust(2)
    return builder.as_markup()


def profile_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text='Редагувати профіль', callback_data=ProfileCallbackFactory(action='edit'))
    builder.button(text='Видалити профіль', callback_data=ProfileCallbackFactory(action='delete'))

    builder.adjust(2)
    return builder.as_markup()


def category_test_kb():
    builder = InlineKeyboardBuilder()

    builder.button(text='Дім', callback_data=TrackerCallbackFactory(
        action='expense',
        category='home'
    )
                   )

    builder.button(text='Авто', callback_data=TrackerCallbackFactory(
        action='expense',
        category='auto'
    )
                   )

    builder.adjust(2)
    return builder.as_markup()


def subcategory_test_kb():
    builder = InlineKeyboardBuilder()

    builder.button(text='Оренда', callback_data=TrackerCallbackFactory(
        action='expense',
        category='home',
        subcategory='rent'
    )
                   )

    builder.button(text='Комуналка', callback_data=TrackerCallbackFactory(
        action='expense',
        category='auto',
        subcategory='com'
    )
                   )

    builder.adjust(2)
    return builder.as_markup()
