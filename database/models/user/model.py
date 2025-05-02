from ...database import Base, created_at, updated_at, bigint_pk
from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class User(Base):
    __tablename__ = 'user'

    chat_id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    wb_token: Mapped[str] = mapped_column(nullable=True)
    stable_expence: Mapped[int] = mapped_column(server_default='0')
    variable_expence: Mapped[int] = mapped_column(server_default='0')
    is_user: Mapped[bool]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]