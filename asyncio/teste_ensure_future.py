#!/usr/bin/python3
# coding: utf-8

import asyncio
import sys

@asyncio.coroutine
def forever():
    count = 0
    while True:
        try:
            msg = "Waiting {}".format(count) 
            print(msg, end='')
            sys.stdout.flush()
            yield from asyncio.sleep(.4)
            print("\x08" * len(msg), end='')
            count += 1
        except asyncio.CancelledError:
            break
    return count


@asyncio.coroutine
def enrola():
    print("BEGIN enrolando")
    yield from asyncio.sleep(5)
    print("\nEND enrolando")

def main():
    future = asyncio.ensure_future(forever())
    yield from enrola()
    future.cancel()
    result = yield from future
    return result

loop = asyncio.get_event_loop()
result = loop.run_until_complete(main())
print("RESULTADO", result)
loop.close()
