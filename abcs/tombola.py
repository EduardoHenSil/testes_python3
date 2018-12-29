#!/usr/bin/python3
# coding: utf-8

import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Adiciona itens a partir de um iterável"""

    @abc.abstractmethod
    def pick(self):
        """Remove um item aleatóriamente, devolvendo-o.
           Este método deve levantar 'LookupError' quando a instância estiver vazia"""

    def loaded(self):
        """Devolve 'True' se houver pelo menos um item, 'False' caso contrário."""
        return bool(self.inspect())

    def inspect(self):
        """Devolve uma tupla ordenada com os itens contidos no momento"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))
