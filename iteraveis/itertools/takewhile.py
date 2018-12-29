#!/usr/bin/python3
# coding: utf-8

import itertools

gen = itertools.takewhile(lambda n: n < 10, itertools.count(1, .5))
print(list(gen))
