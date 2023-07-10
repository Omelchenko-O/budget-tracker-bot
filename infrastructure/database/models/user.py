from infrastructure.database.models.base import Base, TableNameMixin, TimestampMixin, int_pk


class User(Base, TableNameMixin, TimestampMixin):
    id: int_pk
    username: str
    city: str
