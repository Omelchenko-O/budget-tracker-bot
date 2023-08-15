from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import Base, TimestampMixin, int_pk, str_100


class ExpenseSubCategory(Base, TimestampMixin):
    __tablename__ = 'expense_subcategories'

    subcategory_id: Mapped[int_pk]
    name: Mapped[str_100]
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('expense_categories.category_id'))

    categories = relationship("ExpenseCategory", back_populates="subcategories")

    def __repr__(self):
        return f"<Expense category {self.category_id} {self.name}>"
