#!/usr/bin/python3
# coding: utf-8

def make_average():
    series = []
    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return average

