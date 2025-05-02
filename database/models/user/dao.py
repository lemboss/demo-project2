from ...database import async_session_maker
from ...dao import BaseDAO
from .model import User

class UserDAO(BaseDAO):
    model = User
