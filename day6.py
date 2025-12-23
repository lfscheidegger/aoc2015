#!/usr/bin/python3

from collections import defaultdict
from dataclasses import dataclass
from typing import Generator, Tuple

import sys


@dataclass(frozen = True)
class Instruction:
    kind: str
    bounds: Tuple[int, int, int, int]

    @staticmethod
    def from_input_line(line: str) -> 'Instruction':
        if line.startswith('toggle '):
            kind = 'toggle'
            line = line[7:]
        elif line.startswith('turn off '):
            kind = 'off'
            line = line[9:]
        elif line.startswith('turn on '):
            kind = 'on'
            line = line[8:]
        else:
            raise RuntimeError(f'Unexpected instruction: {line}')

        first, _, second = line.split()
        first, second = first.split(','), second.split(',')
            
        return Instruction(kind, tuple(int(x) for x in first + second))

    def gen_lights(self):
        for x in range(self.bounds[0], self.bounds[2] + 1):
            for y in range(self.bounds[1], self.bounds[3] + 1):
                yield x, y


def part1() -> int:
    instructions = [Instruction.from_input_line(line) for line in sys.stdin]

    lights = defaultdict(bool)
    for instruction in instructions:
        for light in instruction.gen_lights():            
            lights[light] = True if instruction.kind == 'on' else False if instruction.kind == 'off' else not lights[light]

    return sum(lights.values())


def part2() -> int:
    instructions = [Instruction.from_input_line(line) for line in sys.stdin]

    lights = defaultdict(int)
    for instruction in instructions:
        for light in instruction.gen_lights():            
            lights[light] += 1 if instruction.kind == 'on' else -1 if instruction.kind == 'off' else 2
            lights[light] = max(lights[light], 0)

    return sum(lights.values())


print(part2())
