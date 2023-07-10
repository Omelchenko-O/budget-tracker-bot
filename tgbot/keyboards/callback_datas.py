from typing import Optional

from aiogram.filters.callback_data import CallbackData


class TrackerCallbackFactory(CallbackData, prefix='tracker'):
    action: str
    category: Optional[str]
    subcategory: Optional[str]
    income_source: Optional[str]


class ProfileCallbackFactory(CallbackData, prefix='profile'):
    action: str
