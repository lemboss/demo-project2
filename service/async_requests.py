import aiohttp

class AsyncRequests:
    session = None

    @classmethod
    async def initialize_session(cls):
        cls.session = aiohttp.ClientSession()

    @classmethod
    async def close_session(cls):
        await cls.session.close()

    @classmethod
    async def get(cls, url: str, params: dict = {}, headers: dict = {}):
        async with cls.session.get(url=url, params=params, headers=headers) as resp:
            return await resp.text()
        
    @classmethod
    async def get_proxy(cls, url: str, proxy: str, params: dict = {}, headers: dict = {}):
        async with cls.session.get(url=url, params=params, headers=headers, proxy=proxy) as resp:
            return await resp.text()
        
    @classmethod
    async def post(cls, url: str, params: dict = {}, body: dict = {}, headers: dict = {}):
        async with cls.session.post(url=url, params=params, data=body, headers=headers) as resp:
            if resp.status == 200:
                return await resp.json()

    @classmethod
    async def put(cls, url: str, params: dict = {}, data: dict = {}, headers: dict = {}):
        async with cls.session.put(url=url, params=params, data=data, headers=headers) as resp:
            return await resp.read()
