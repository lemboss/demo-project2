import hashlib
import json
from service.async_requests import AsyncRequests
from config.config import settings
from copy import copy, deepcopy

class TBankCash:
    
    @classmethod
    def generate_sign(cls, payload: dict):
        sha256_hash = hashlib.sha256()
        data = dict(sorted(payload.items()))
        line = "".join(''.join(str(x) for x in data.values()))
        sha256_hash.update(line.encode('utf-8'))
        sign = sha256_hash.hexdigest()
        
        return sign
    
    @classmethod
    async def create_payment(cls, amount, order_id):
        amount *= 100
        ...
        url = "https://securepay.tinkoff.ru/v2/Init"
        res = await AsyncRequests.post(url=url, body=data, headers=headers)
        if "Success" in res and res["Success"]:
            return res
        
        