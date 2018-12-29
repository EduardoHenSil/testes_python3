#!/usr/bin/python3
# coding: utf-8

import itertools

# filterfalse(predicate, it) Aplica predicate a cada item de it, entregando o item se predicate(item) for falso.

def is_vowel(c):
    return c.lower() in 'aeiou'

print(list(itertools.filterfalse(is_vowel, 'Aardvark')))
