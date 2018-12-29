#!/usr/bin/python3
# coding: utf-8

from functools import wraps

def coroutine(func):    
    """Decorator: prepara 'func' fazendo-a avançar até o primeiro `yield` """

    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

