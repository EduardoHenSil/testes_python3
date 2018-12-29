#!/usr/bin/python3
# coding: utf-8

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = "Plase DO NOT divide by zero!"
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

