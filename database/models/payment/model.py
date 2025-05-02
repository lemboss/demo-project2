from ...database import Base, created_at, updated_at, bigint_pk
from sqlalchemy import BIGINT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime

class Payment(Base):
    __tablename__ = 'payment'

    id: Mapped[bigint_pk] 
    chat_id: Mapped[int] = mapped_column(BIGINT)
    status: Mapped[str] = mapped_column(nullable=True)
    payment_id: Mapped[str] = mapped_column(BIGINT)
    expiration_at: Mapped[datetime] = mapped_column(nullable=True)
    created_at: Mapped[created_at]