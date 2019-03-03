#!/usr/bin/python3

import sys
import asyncio
from charfinder import UnicodeNameIndex

CRLF = b'\r\n'
PROMPT = b'?>'

index = UnicodeNameIndex()

async def handle_queries(reader, writer):
    while True:
        writer.write(PROMPT) # não pode usar await (yield from)
        try:
            await writer.drain() # presico usar await (yield from)
            data = await reader.readline()
        except ConnectionResetError:
            break

        try:
            query = data.decode().strip()
        except UnicodeDecodeError:
            query = '\x00'

        client = writer.get_extra_info('peername')
        print('Received from {}: {!r}'.format(client, query))
        if query:
            if ord(query[:1]) < 32:
                break
            lines = list(index.find_description_strs(query))
            if lines:
                writer.writelines(line.encode() + CRLF for line in lines)
            writer.write(index.status(query, len(lines)).encode() + CRLF)

            await writer.drain()
            print('Sent {} results'.format(len(lines)))
    print('Close the client socket')
    writer.close()


def main(address='127.0.0.1', port=2323):
    port = int(port)

    # Montando o servidor TCP
    loop = asyncio.get_event_loop()

    # asyncio.start_server devolve uma instancia de asyncio.Server (servidor socket TCP)
    server_coro = asyncio.start_server(handle_queries, address, port, loop=loop)

    # ativa a instancia se asyncio.Server
    server = loop.run_until_complete(server_coro)

    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL+C to stop.'.format(host))
    try:

        # bloqueia main até CTRL+C (execução do loop de eventos)
        loop.run_forever()

    except KeyboardInterrupt: # CTRL+C pressionado
        pass

    print('Server shutting down.')
    server.close()

    # server.wait_closed() devolve um future
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])

