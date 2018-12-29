#!/usr/bin/python3
# coding: utf-8

import itertools

summary ="""
itertools.islice(it, stop) ou itertools.islice(it, start, stop, step=1)
Produz um fatia de it, semelhante a s[:stop] ou s[start:stop:step], exceto que it pode ser qualquer
iteravel e a operação é lazy.
"""
print(summary)
print("Ex:")
print("itertools.islice('Aardvark', 5)", "-->", list(itertools.islice('Aardvark', 5)))
print("itertools.islice('Aardvark', 1, 7, 2)", "-->", list(itertools.islice('Aardvark', 1, 7, 2)))

