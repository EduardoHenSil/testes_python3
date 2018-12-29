#!/usr/bin/python3
# coding: utf-8

import os
import time
import sys
import threading

import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR').split()
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads/'

res = []

def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)

def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content

def show(text):
    print(text, end=' ')
    sys.stdout.flush()

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    res.append(cc)

def download_many(cc_list):
    for cc in sorted(cc_list):
        t = threading.Thread(target=download_one, args=(cc,))
        t.start()

def main(download_many):
    t0 = time.time()
    download_many(POP20_CC)
    while len(res) < 20:
        continue
    elapsed = time.time() - t0
    msg = '\n{} flags downloaded in {:.2f}s'
    print(msg.format(20, elapsed))

if __name__ == '__main__':
    main(download_many)

