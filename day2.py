#!/usr/bin/python3

import sys

from typing import Tuple


def parse_line(line: str) -> Tuple[int, int, int]:
    x, y, z = line.split('x')
    return int(x), int(y), int(z)


def wrapping_paper_needed(box: Tuple[int, int, int]) -> int:
    w, h, l = box

    return 2*l*w + 2*w*h + 2*h*l + min(w * h, w * l, h * l)


def ribbon_needed(box: Tuple[int, int, int]) -> int:
    w, h, l = box

    return 2 * min(w + h, w + l, h + l) + w * h * l


def part1() -> int:
    return sum(map(lambda l: wrapping_paper_needed(parse_line(l)), sys.stdin))


def part2() -> int:
    return sum(map(lambda l: ribbon_needed(parse_line(l)), sys.stdin))


print(part2())
