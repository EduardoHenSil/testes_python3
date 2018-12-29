#!/usr/bin/python3
# coding: utf-8

def fibonacci(end):
    a, b = 0, 1
    while a <= end:
        yield a
        a, b = b, a + b
