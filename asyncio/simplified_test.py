import asyncio
import aiohttp
from aiohttp import web


@asyncio.coroutine
async def http_get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                ctype = response.headers.get('Content-Type', '').lower()
                if 'json' in ctype or url.endswith('json'):
                    data = await response.json()
                else:
                    data = await response.read()
                return data
            elif response.status == 404:
                raise web.HTTPNotFound
            else:
                raise aiohttp.errors.HttpProcessingError(
                        code = response.status,
                        message = response.reason,
                        headers = response.headers
                        )


@asyncio.coroutine
async def teste():
    try:
        data = await http_get('http://flupy.org/data/flags/br/metadata.json')
    except Exception as e:
        print(e)
    else:
        print(data)

loop = asyncio.get_event_loop()
loop.run_until_complete(teste())
loop.close()
