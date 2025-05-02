from ...database import async_session_maker
from sqlalchemy import select, desc, insert, update, func
from ...dao import BaseDAO
from .model import Payment

class PaymentDAO(BaseDAO):
    model = Payment
    
    @classmethod
    async def find_sub(cls, chat_id):
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__.columns)
                .filter(cls.model.chat_id==chat_id, cls.model.expiration_at.is_not(None))
                .order_by(desc(cls.model.id))
            )
            result = await session.execute(query)
            return result.mappings().first()
