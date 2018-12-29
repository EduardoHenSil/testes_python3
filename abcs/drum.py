#!/usr/bin/python3
# coding: utf-8

import random
from tombola import Tombola

class TumblingDrum(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty TumblingDrum')

    def __call__(self):
        self.pick()
