from ...database import Base, int_pk, created_at
from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class UserVariableExpence(Base):
    __tablename__ = 'user_variable_expence'

    id: Mapped[int_pk]
    chat_id: Mapped[int]
    expence: Mapped[int]
    created_at: Mapped[created_at]