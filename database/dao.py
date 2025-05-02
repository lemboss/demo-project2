from .database import async_session_maker
from sqlalchemy import select, desc, insert, update, func
from sqlalchemy.exc import IntegrityError

class BaseDAO:
    model = None
        
    @classmethod
    async def find_all(cls, *args):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter(*args)
            result = await session.execute(query)
            return result.mappings().all()
    
    @classmethod
    async def find_last(cls, *args):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter(*args).order_by(desc(cls.model.id))
            result = await session.execute(query)
            return result.mappings().first()
    
    @classmethod
    async def find_first(cls, *args):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter(*args).order_by()
            result = await session.execute(query)
            return result.mappings().first()
        
    @classmethod
    async def get_count(cls, *args):
        async with async_session_maker() as session:
            query = select(func.count()).select_from(cls.model).filter(*args)
            result = await session.execute(query)
            return result.scalar()
        
    @classmethod
    async def get_count_distinct(cls, column: str, *args):
        async with async_session_maker() as session:
            query = select(func.count(func.distinct(getattr(cls.model, column)))).filter(*args)
            result = await session.execute(query)
            return result.scalar()
        
    
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = (
                insert(cls.model)
                .values(**data)
                .returning(cls.model)
            )
            try:
                new_data = await session.execute(query)
                await session.commit()
                return new_data.mappings().all()
            except IntegrityError as e:
                await session.rollback()
                return e
        
    @classmethod
    async def update(cls, *condition, **data):
        async with async_session_maker() as session:
            query = (
                update(cls.model)
                .where(*condition)
                .values(**data)
                .returning(cls.model)
            )
            try:
                updates = await session.execute(query)
                await session.commit()
                return updates.scalars().all()
            except IntegrityError:
                await session.rollback()
                return []