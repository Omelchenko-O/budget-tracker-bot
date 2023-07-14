from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import Base, TableNameMixin, TimestampMixin


class User(Base, TableNameMixin, TimestampMixin):
    id: Mapped[int] = mapped_column(primary_key=True, type_=BigInteger)
    telegram_id: Mapped[int] = mapped_column()
    username: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
