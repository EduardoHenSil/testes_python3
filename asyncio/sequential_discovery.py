#!/usr/bin/python3
#coding: utf-8

import sys
from time import time
from collections import namedtuple
import requests


RESULT_FMT = '{} | {}' # formatação do output de resultados.
                       # Utilizado no método 'print_result'

BREAK_LINE = '\n'
CARRIAGE_RETURN = '\r'
REPLACE_LIST = [BREAK_LINE, CARRIAGE_RETURN] # lista de caracteres que devem ser retirados das palavras da
                                             # wordlist antes do request ser realizado. Utilizado no método 'sanitize'

Status = namedtuple('Status', 'url code') # representa o status final de cada request


def sanitize(word):
    for replace in REPLACE_LIST:
        word = word.replace(replace, '')
    return word


def read_wordlist(wordlist):
    with open(wordlist) as fd:
        while True:
            word = fd.readline()
            if word:
                if BREAK_LINE == word:
                    continue
                yield sanitize(word)
            else:
                break


def print_result(status):
    print(RESULT_FMT.format(status.url, status.code))


def fetch(url):
    response = requests.get(url)
    return Status(url, response.status_code)


def discover(url, wordlist):
    for path in read_wordlist(wordlist):
        status = fetch(url + path)

        #if status.code >= 200 and status.code < 300:
        print_result(status)


def main(url, wordlist):
    if not url.endswith("/"):
        url += "/"

    discover(url, wordlist)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Example: {} http://google.com /usr/share/wordlist/lista.txt".format(sys.argv[0]))
        exit()
    t0 = time()
    main(url=sys.argv[1], wordlist=sys.argv[2])
    t1 = time() - t0
    print("Duração {:.2f}s".format(t1))

