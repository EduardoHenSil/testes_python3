#!/usr/bin/python3
# coding: utf-8

from collections import abc

class FrozenJSON:
    """Uma fachada somente de leitura para navegar por um 
       objeto JSON ou similar usando notação de atributo
    """

    def __init__(self, mapping):
        self._data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            return FrozenJSON.build(self._data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj
