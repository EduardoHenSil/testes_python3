#!/usr/bin/python3
# coding: utf-8

import doctest
import sys, os

if len(sys.argv) != 2 or not os.path.exists(sys.argv[1]):
    print("Ex: {} {}".format(sys.argv[0], 'doctest.rst'))
    print("doctest.rst deve ser um arquivo doctest já devidamente criado!")
    exit()

test_file = sys.argv[1]

res = doctest.testfile(test_file, verbose=True, optionflags=doctest.REPORT_ONLY_FIRST_FAILURE)
print(res)
