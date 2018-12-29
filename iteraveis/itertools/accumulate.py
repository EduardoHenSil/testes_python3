#!/usr/bin/python3
# coding: utf-8

import itertools
import operator

summary = """
itertools.accumulate(it, [func])
Produz somas accumuladas; se func for especificada, entrega o resultado da sua aplicação
ao primeiro par de itens de it, em seguida ao primeiro resultado e o próximo item.
Diferente da função functools.reduce, accumulate gera os valores a cada resultado.
"""


print(summary)

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

print("sample =", sample)
print("itertools.accumulate(sample) -->", list(itertools.accumulate(sample)))
print("itertools.accumulate(sample, operator.mul) -->", list(itertools.accumulate(sample, operator.mul)))
