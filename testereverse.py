#!/usr/bin/python3

class Set0(set):

    def __and__(self, conj):
        print("Chamando &")
        return set.__and__(self, conj)

    def __rand__(self, conj):
        print("Chamando r&")
        return set.__rand__(self, conj)
