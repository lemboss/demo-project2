from cryptography.fernet import Fernet
from config.config import settings

class PassEncryptor:
    
    @classmethod
    async def initialize(cls):
        cls._cipher = Fernet(settings.key.encode())
        
    @classmethod
    async def encrypt(cls, api_key: str) -> str:
        if api_key:
            return cls._cipher.encrypt(api_key.encode()).decode()
        
    @classmethod
    async def decrypt(cls, encrypted_key: str) -> str:
        if encrypted_key:
            return cls._cipher.decrypt(encrypted_key).decode()