from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from magic_filter import F

from tgbot.keyboards.callback_datas import TrackerCallbackFactory
from tgbot.keyboards.inline import budget_tracker_keyboard, category_test_kb, subcategory_test_kb
from tgbot.misc.states import Tracker

user_tracker_router = Router()


@user_tracker_router.message(Command('tracker'))
async def tracker(message: Message, state: FSMContext):
    await message.answer('Яку дію ви хочете зробити?', reply_markup=budget_tracker_keyboard())
    await state.set_state(Tracker.action)


@user_tracker_router.callback_query(Tracker.action, TrackerCallbackFactory.filter(F.action == 'expense'))
async def tracker_category(call: CallbackQuery, state: FSMContext, callback_data: TrackerCallbackFactory):
    await call.message.edit_text('Оберіть категорію витрат зі списку:', reply_markup=category_test_kb())

    await call.answer()
    await state.set_state(Tracker.category)


@user_tracker_router.callback_query(Tracker.category, TrackerCallbackFactory.filter(F.category == 'home'))
async def tracker_subcategory(call: CallbackQuery, state: FSMContext, callback_data=TrackerCallbackFactory):
    await state.update_data(category=callback_data.category)

    await call.message.edit_text('Оберіть підкатегорію витрат:', reply_markup=subcategory_test_kb())

    await call.answer()
    await state.set_state(Tracker.subcategory)


@user_tracker_router.callback_query(Tracker.subcategory, TrackerCallbackFactory.filter(F.action == 'expense'))
async def tracker_amount(call: CallbackQuery, state: FSMContext, callback_data=TrackerCallbackFactory):
    await state.update_data(subcategory=callback_data.subcategory)

    await call.message.edit_text('Вкажіть суму витрати (лише число):')

    await call.answer()
    await state.set_state(Tracker.amount)


@user_tracker_router.message(Tracker.amount)
async def tracker_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    data = await state.get_data()

    await message.answer(f'Витрату збережено: {data["category"], data["subcategory"], data["amount"]}',
                         reply_markup=budget_tracker_keyboard())

    await state.clear()
