#!/usr/bin/python3
"""Cria um indice que mapeia palavra -> lista de ocorrencias"""
import sys
import re
WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # forma correta
            index.setdefault(word, []).append(location)
# exibe em ordem alfabetica
for word in sorted(index, key=str.upper):
    print(word, index[word])
