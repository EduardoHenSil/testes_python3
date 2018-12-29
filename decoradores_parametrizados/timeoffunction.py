#!/usr/bin/python3
# coding: utf-8

import time
from functools import wraps

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):

    def decorator(func):

        @wraps(func)
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = []
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))

            if kwargs:
                pairs = ['%s=%s' % (k, w) for k, w in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))

            arg_str = ', '.join(arg_lst)
            print(fmt.format(**locals()))
            return result
        return clocked
    return decorator
