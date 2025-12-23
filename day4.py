#!/usr/bin/python3

from hashlib import md5
import sys


INPUT = "yzbqklnj"


def part1():
    guess = 1
    while True:
        if md5(f'{INPUT}{guess}'.encode('ascii')).hexdigest().startswith('00000'):
            return guess

        guess += 1


def part2():
    guess = 1
    while True:
        if md5(f'{INPUT}{guess}'.encode('ascii')).hexdigest().startswith('000000'):
            return guess

        guess += 1        


print(part2())
