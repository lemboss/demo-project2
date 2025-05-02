import os
from datetime import datetime, timedelta
from config.config import settings
from io import BytesIO
from .security import PassEncryptor
from database.models.user.dao import UserDAO
from database.models.payment.dao import PaymentDAO
from database.models.user_variable_expence.dao import UserVariableExpenceDAO
from tgbot.media.path import path
import aiofiles
from typing import Literal
from aiocache import cached, Cache
from cache import cache

class UserData: 

    @classmethod
    async def add_user(cls, chat_id: int, key: str = None):
        await UserDAO.add(
            chat_id=chat_id,
            wb_token=key,
            is_user=True
        )
        
    @classmethod
    async def add_payment(cls, chat_id: int, status: Literal["free", "sub"], period: int):
        info = await cls.get_payment(chat_id)
        if info: return 
        
        await PaymentDAO.add(
            chat_id=chat_id,
            status=status,
            payment_id=0,
            expiration_at=datetime.now()+timedelta(days=period)
        )
        
    @classmethod
    async def get_payment(cls, chat_id: int):
        return await PaymentDAO.find_sub(chat_id=chat_id)
    
    @classmethod
    async def set_file(cls, chat_id: int, data: BytesIO):
        """
        пока на 1 пользователя - 1 файл
        """
        file_path = "tgbot/storage/" + f"{chat_id}.bin"
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(data.getvalue()) 
    
    @classmethod
    async def get_example_file(cls) -> BytesIO:
        file_path = path.doc.example
        if os.path.isfile(file_path):
            async with aiofiles.open(file_path, "rb") as file:
                content = await file.read()
                return BytesIO(content)
    
    @classmethod
    async def get_file(cls, chat_id: int) -> BytesIO:
        file_path = "tgbot/storage/" + f"{chat_id}.bin"
        if os.path.isfile(file_path):
            async with aiofiles.open(file_path, "rb") as file:
                content = await file.read()
                return BytesIO(content)
        
    @classmethod
    async def get_user(cls, chat_id: int):
        return await UserDAO.find_first(UserDAO.model.chat_id==chat_id)
        
    @classmethod
    async def get_key(cls, chat_id: int):
        user = await cls.get_user(chat_id)
        token = await PassEncryptor.decrypt(user["wb_token"])
        if token:
            return token
        
    @classmethod
    async def set_key(cls, chat_id: int, key: str):
        encrypted_key = await PassEncryptor.encrypt(key)
        await UserDAO.update(UserDAO.model.chat_id==chat_id, wb_token=encrypted_key)
        
    @classmethod
    async def get_stable_expence(cls, chat_id: int) -> int:
        user = await cls.get_user(chat_id)
        return user["stable_expence"]
        
    @classmethod
    async def set_stable_expence(cls, chat_id: int, stable_expence: int):
        if -2147483648 > stable_expence or 2147483647 < stable_expence:
            stable_expence = 0
        await UserDAO.update(UserDAO.model.chat_id==chat_id, stable_expence=stable_expence)
        
    @classmethod
    async def get_variable_expence(cls, chat_id: int) -> int:
        user = await cls.get_user(chat_id)
        return user["variable_expence"]
        
    @classmethod
    async def set_variable_expence(cls, chat_id: int, variable_expence: int):
        if -2147483648 > variable_expence or 2147483647 < variable_expence:
            variable_expence = 0
        await UserDAO.update(UserDAO.model.chat_id==chat_id, variable_expence=variable_expence)
                
    @classmethod
    async def update_user(cls, chat_id: int, **kwargs):
        await UserDAO.update(UserDAO.model.chat_id==chat_id, updated_at=datetime.now(), **kwargs)
        
    @classmethod
    async def add_variable_expence(cls, chat_id: int, variable_expence: int):
        await UserVariableExpenceDAO.add(chat_id=chat_id, expence=variable_expence)
        
         