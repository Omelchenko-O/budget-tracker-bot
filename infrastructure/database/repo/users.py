from sqlalchemy import insert

from infrastructure.database.models.user import User
from infrastructure.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def create_user(self, telegram_id: int, username: str, city: str):
        stmt = insert(User).values(
            telegram_id=telegram_id,
            username=username,
            city=city
        )
        await self.session.execute(stmt)
        await self.session.commit()
