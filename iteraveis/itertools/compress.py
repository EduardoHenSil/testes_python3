#!/usr/bin/python3
# coding: utf-8

import itertools

# itertools.compress(it, selector_it) //Consome dois iteraveis em paralelo;
# entrega itens de it sempre que o item correspondente em selector_it for verdadeiro

print(list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1))))
