#!/usr/bin/python3
# coding: utf-8

import sys
import asyncio
import aiohttp
from aiohttp import web
from charfinder import *

index = UnicodeNameIndex()
CONTENT_TYPE = 'text/html'
ROW_TPL = "{} {} {}"
template = """<html>
                <head>
                    <title>HTTP Charfinder</title>
                </head>
                <body>
                    <h1>{query}</h1>
                    <p>{result}</p>
                    
                    <h3>{message}</h3>
                </body>
              </html>
           """

def home(request):
    try:
        query = request.query['query']
    except KeyError:
        query = ''
    print('Query: {!r}'.format(query))
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '<br/>'.join(ROW_TPL.format(descr.code_str, descr.char, descr.name) for descr in descriptions)
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing caracters.'
    html = template.format(query=query, result=res, message=msg)
    print('Sending {} results.'.format(len(descriptions)))
    return web.Response(content_type=CONTENT_TYPE, text=html)


async def init(loop, address, port):
    app = web.Application(loop=loop)
    app.router.add_routes([web.get('/', home)])
    handler = app.make_handler()
    server = await loop.create_server(handler, address, port)
    return server.sockets[0].getsockname()


def main(address='127.0.0.1', port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))
    print('Serving on {}. Hit CTRL+C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt: # CTRL+C pressionado
        pass
    print('Server shutting down.')
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])

