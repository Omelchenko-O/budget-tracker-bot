from sqlalchemy.orm import Mapped, relationship

from infrastructure.database.models.base import Base, TimestampMixin, int_pk, str_100


class ExpenseCategory(Base, TimestampMixin):
    __tablename__ = 'expense_categories'

    category_id: Mapped[int_pk]
    name: Mapped[str_100]

    subcategories = relationship("ExpenseSubCategory", back_populates="category")

    def __repr__(self):
        return f"<Expense category {self.category_id} {self.name}>"
