#!/usr/bin/env python3
import fileinput
from functools import reduce
from operator import mul


def pad(arr):
    tmp = [[9] + row + [9] for row in arr]
    pad_row = [9] * len(tmp[0])
    return [pad_row, *tmp, pad_row]


def neighbors(y, x):
    for yi, xi in zip((0, 0, -1, 1), (-1, 1, 0, 0)):
        yield (y + yi, x + xi)


def find_minima(data):
    return [
        (y, x)
        for y in range(1, len(data) - 1)
        for x in range(1, len(data[y]) - 1)
        if data[y][x] < min(data[yi][xi] for yi, xi in neighbors(y, x))
    ]


def part1(data):
    min_vals = [data[y][x] for y, x in find_minima(data)]
    return sum(min_vals) + len(min_vals)


def part2(data):
    minima = find_minima(data)
    basins = []
    for pos in minima:
        basin = [pos]
        for (y, x) in basin:
            basin += list(
                filter(
                    lambda e: data[e[0]][e[1]] < 9 and e not in basin,
                    [(yi, xi) for yi, xi in neighbors(y, x)],
                )
            )
        basins.append(basin)
    return reduce(mul, sorted(map(len, basins))[-3:])


def main():
    data = pad([list(map(int, list(line.rstrip()))) for line in fileinput.input()])
    print(part1(data))
    print(part2(data))


main()
