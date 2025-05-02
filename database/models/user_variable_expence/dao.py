from sqlalchemy import select, desc, insert, update, func
from ...database import async_session_maker
from ...dao import BaseDAO
from .model import UserVariableExpence


class UserVariableExpenceDAO(BaseDAO):
    model = UserVariableExpence

    @classmethod
    async def get_sum_expence_variable_by_period(cls, *args):
        async with async_session_maker() as session:
            query = select(func.sum(cls.model.expence)).filter(*args)
            result = await session.execute(query)
            return result.scalar()