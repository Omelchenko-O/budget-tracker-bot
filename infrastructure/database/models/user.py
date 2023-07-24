from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from infrastructure.database.models.base import Base, TableNameMixin, TimestampMixin, int_pk, str_100


class User(Base, TableNameMixin, TimestampMixin):
    # user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    user_id: Mapped[int_pk]
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str_100]
    city: Mapped[str_100]

    def __repr__(self):
        return f"<User {self.user_id} {self.username} {self.city}>"
