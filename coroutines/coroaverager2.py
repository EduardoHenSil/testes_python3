#!/usr/bin/python3
# coding: utf-8

from collections import namedtuple

Result = namedtuple('Result', 'count averager')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)
