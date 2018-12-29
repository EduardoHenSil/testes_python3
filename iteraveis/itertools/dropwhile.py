#!/usr/bin/python3
# coding: utf-8

import itertools

# itertools.dropwhile(predicate, it) Consome it descartando itens enquanto "predicate" for avaliado
# como verdadeiro, em seguida, produz todos os itens restantes (novas verificações não são feitas)

def is_vowel(c):
    return c.lower() in 'aeiou'


print(list(itertools.dropwhile(is_vowel, 'Aardvark')))
