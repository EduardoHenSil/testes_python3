#!/usr/bin/python3
# conding: utf-8

import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        yield from RE_WORD.finditer(self.text)
