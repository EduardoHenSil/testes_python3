#!/usr/bin/python3

import time


class Foo:

    def __init__(self):
        self.seq = [0, 10, 20, 30]

    def __getitem__(self, pos):
        return self.seq[pos]


class Foo1:

    def __init__(self):
        self.seq = [0, 10, 20, 30]

    def __getitem__(self, pos):
        return self.seq[pos]

    def __len__(self):
        return len(self.seq)


fslen = Foo()
fclen = Foo1()

start = time.clock()
fslen[3]
elapsed = time.clock()
elapsed = elapsed - start
print("f[3] SEM __len__ -> {}".format(elapsed))


start = time.clock()
fclen[3]
elapsed = time.clock()
elapsed = elapsed - start
print("f[3] COM __len__ -> {}".format(elapsed))
