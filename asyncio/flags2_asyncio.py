#!/usr/bin/python3
# coding: utf-8

import asyncio
import collections

import aiohttp
from aiohttp import web
import tqdm
from flags2_common import main, HTTPStatus, Result, save_flag


# default definido com um valor baixo para evitar erros do site remoto, por exemplo
# 503 - Service Temporarily Unavailable (Serviço Temporariamente Indisponível)
DEFAULT_CONCUR_REQ = 5
MAX_CONCUR_REQ = 1000

class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


@asyncio.coroutine
def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)

    if resp.status == 200:
        image = yield from resp.read()
        return image

    elif resp.status == 404:
        raise web.HTTPNotFound()

    else:
        raise aiohttp.HttpProcessingError(code=resp.status,
                                          message=resp.reason,
                                          headers=resp.headers
                                          )


@asyncio.coroutine
def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):
            image = yield from get_flag(base_url, cc)

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
def download_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose) for cc in sorted(cc_list)]
    to_do_iter = asyncio.as_completed(to_do)

    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))

    for future in to_do_iter:
        try:
            res = yield from future

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
    coro = download_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()

    return counts

if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
