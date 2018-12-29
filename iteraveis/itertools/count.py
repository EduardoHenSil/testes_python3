#!/usr/bin/python3
# coding: utf-8

import itertools

gen = itertools.count(1, .5)

number = next(gen)
print("primeiro: -->>", number)


for number in gen:
    print("-->>", number)
    if number >= 10:
        break
