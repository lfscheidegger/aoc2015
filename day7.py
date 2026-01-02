#!/usr/bin/python3

from dataclasses import dataclass
from functools import cache
import sys


def part1():
    lines = [line for line in sys.stdin]
        
    @cache
    def destination_for_line(line: str) -> str:
        _, right = line.split('->')
        right = right.strip()
        return right

    @cache
    def line_for_destination(destination: str) -> str:
        candidates = list(filter(lambda line: destination_for_line(line) == destination, lines))
        assert len(candidates) == 1
        return candidates[0]    

    @cache
    def solve_line(line: str) -> int:
        left, _ = line.split('->')
        left = left.strip()
        tokens = left.split()

        if len(tokens) == 1:
            left = tokens[0]
            if left.isnumeric():
                return int(left)
            else:
                return solve_line(line_for_destination(left))

        if len(tokens) == 2:
            assert tokens[0] == 'NOT'
            return ~solve_line(line_for_destination(tokens[1]))

        assert len(tokens) == 3
        if tokens[1] == 'RSHIFT':
            amount = int(tokens[2])
            return solve_line(line_for_destination(tokens[0])) >> amount

        elif tokens[1] == 'LSHIFT':
            amount = int(tokens[2])
            return solve_line(line_for_destination(tokens[0])) << amount

        elif tokens[1] == 'OR':
            left = int(tokens[0]) if tokens[0].isnumeric() else solve_line(line_for_destination(tokens[0]))
            right = int(tokens[2]) if tokens[2].isnumeric() else solve_line(line_for_destination(tokens[2]))
            return left | right

        elif tokens[1] == 'AND':
            left = int(tokens[0]) if tokens[0].isnumeric() else solve_line(line_for_destination(tokens[0]))
            right = int(tokens[2]) if tokens[2].isnumeric() else solve_line(line_for_destination(tokens[2]))
            return left & right

    return solve_line(line_for_destination('a'))


def part2():
    lines = [line for line in sys.stdin]
        
    @cache
    def destination_for_line(line: str) -> str:
        _, right = line.split('->')
        right = right.strip()
        return right

    @cache
    def line_for_destination(destination: str) -> str:
        candidates = list(filter(lambda line: destination_for_line(line) == destination, lines))
        assert len(candidates) == 1
        return candidates[0]    

    @cache
    def solve_line(line: str) -> int:
        if destination_for_line(line) == 'b':
            return 46065

        left, _ = line.split('->')
        left = left.strip()
        tokens = left.split()

        if len(tokens) == 1:
            left = tokens[0]
            if left.isnumeric():
                return int(left)
            else:
                return solve_line(line_for_destination(left))

        if len(tokens) == 2:
            assert tokens[0] == 'NOT'
            return ~solve_line(line_for_destination(tokens[1]))

        assert len(tokens) == 3
        if tokens[1] == 'RSHIFT':
            amount = int(tokens[2])
            return solve_line(line_for_destination(tokens[0])) >> amount

        elif tokens[1] == 'LSHIFT':
            amount = int(tokens[2])
            return solve_line(line_for_destination(tokens[0])) << amount

        elif tokens[1] == 'OR':
            left = int(tokens[0]) if tokens[0].isnumeric() else solve_line(line_for_destination(tokens[0]))
            right = int(tokens[2]) if tokens[2].isnumeric() else solve_line(line_for_destination(tokens[2]))
            return left | right

        elif tokens[1] == 'AND':
            left = int(tokens[0]) if tokens[0].isnumeric() else solve_line(line_for_destination(tokens[0]))
            right = int(tokens[2]) if tokens[2].isnumeric() else solve_line(line_for_destination(tokens[2]))
            return left & right

    return solve_line(line_for_destination('a'))


print(part2())
