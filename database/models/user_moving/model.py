from ...database import Base, created_at, bigint_pk
from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class UserMoving(Base):
    __tablename__ = 'user_moving'
    
    id: Mapped[bigint_pk]
    chat_id: Mapped[int] = mapped_column(BIGINT)
    step: Mapped[str]
    created_at: Mapped[created_at]