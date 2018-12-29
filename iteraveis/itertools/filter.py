#!/usr/bin/python3
# coding: utf-8

# filter(predicate, it) Aplica predicate a cada item de it, entregando o item se predicate(item) for verdadeiro.

def is_vowel(c):
    return c.lower() in 'aeiou'

print(list(filter(is_vowel, 'Aardvark')))
