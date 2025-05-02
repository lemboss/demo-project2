from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from redis.asyncio import Redis
from .config import settings

if settings.storage.use_redis:
    redis = Redis(host=settings.storage.redis_host, port=settings.storage.redis_port)
    storage = RedisStorage(redis, key_builder=DefaultKeyBuilder(with_destiny=True))
else:
    storage = MemoryStorage()