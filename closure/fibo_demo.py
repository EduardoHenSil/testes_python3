#!/usr/bin/python3
# coding: utf-8

from timeoffunction import *
from functools import lru_cache

@lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__=='__main__':
    print(fibonacci(6))
