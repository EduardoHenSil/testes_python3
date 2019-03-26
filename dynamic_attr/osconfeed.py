#!/usr/bin/python3
# coding: utf-8

from urllib.request import urlopen
import warnings
import os
import json

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
FOLDER = 'data'
JSON = FOLDER + '/osconfeed.json'


if not os.path.exists(FOLDER):
    os.mkdir(FOLDER)


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warning.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)
