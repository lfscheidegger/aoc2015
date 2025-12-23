#!/usr/bin/python3

import sys


def part1() -> int:
    def is_nice(line: str) -> bool:
        if line.find('ab') != -1: return False

        if line.find('cd') != -1: return False

        if line.find('pq') != -1: return False

        if line.find('xy') != -1: return False

        doubled_letters = any(map(lambda dd: dd[0] == dd[1], zip(line, line[1:])))
        if not doubled_letters: return False

        vowel_count = sum(map(lambda c: c in set('aeiou'), line))
        return vowel_count >= 3

    return sum(map(lambda line: is_nice(line), sys.stdin))


def part2() -> int:
    def is_nice(line: str) -> bool:
        has_pairs = False
        all_pairs = [''.join(pair) for pair in zip(line, line[1:])]
        for pair in all_pairs:
            if len(line.replace(pair, '')) <= len(line) - 4:
                has_pairs = True
                break

        has_nested_letter = False
        for idx in range(len(line) - 2):
            if line[idx] == line[idx + 2]:
                has_nested_letter = True
                break

        return has_pairs and has_nested_letter

    return sum(map(lambda line: is_nice(line), sys.stdin))    


print(part2())
