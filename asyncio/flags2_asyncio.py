#!/usr/bin/python3
# coding:utf-8

import asyncio
import collections
import aiohttp
from aiohttp import web
import tqdm
from flags2_common import main, HTTPStatus, Result, save_flag

# default definido com um valor baixo para evitar erros do site remoto, por exemplo
# 503 - Service Temporarily Unavailable (Serviço Temporariamente Indisponivel)
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code

@asyncio.coroutine
async def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image = await response.read()
                return image
            elif response.status == 404:
                raise web.HTTPNotFound()
            else:
                raise aiohttp.HttpProcessingError(
                        code = response.status,
                        message = response.reason,
                        header = response.headers
                        )
@asyncio.coroutine
async def download_one(cc, base_url, semaphore, verbose):
    try:
        async with semaphore:
            image = await get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'

    if verbose and msg:
        print(cc, msg)

    return Result(status, cc)

@asyncio.coroutine
async def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose) for cc in sorted(cc_list)]
    to_do_iter = asyncio.as_completed(to_do)
    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))

    for future in to_do_iter:
        try:
            res = await future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '*** Error for {}: {}'
                print(msg.format(country_code, error_msg))

            status = HTTPStatus.error
        else:
            status = res.status

        counter[status] += 1
    return counter

def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)

