#!/usr/bin/python3
# coding: utf-8

import asyncio


@asyncio.coroutine
def spliter(message):
    as_list = []
    for word in message.split(' '):
        print(word)
        as_list.append(word)
        yield from asyncio.sleep(.1)
    return as_list

@asyncio.coroutine
def delegator(message):
    task_future = [asyncio.ensure_future(spliter(message))]
    counter_task = [asyncio.ensure_future(counter())]
    yield from asyncio.wait(task_future)
    yield from asyncio.wait(counter_task)

@asyncio.coroutine
def counter():
    count = 0;
    while count < 10:
        print(count)
        try:
            yield from asyncio.sleep(.2)
        except asyncio.CancelledError:
            break
        count += 1


loop = asyncio.get_event_loop()
result = loop.run_until_complete(delegator("meu teste minha vida"))
loop.close()
