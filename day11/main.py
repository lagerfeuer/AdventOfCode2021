#!/usr/bin/env python3
import fileinput
from copy import deepcopy


def pprint(data):
    for row in data:
        print("".join([str(e) for e in row]))
    print()


def inc(data):
    for y in range(len(data)):
        for x in range(len(data[y])):
            data[y][x] += 1


def flashing(data):
    return [
        (y, x) for y in range(len(data)) for x in range(len(data[y])) if data[y][x] > 9
    ]


def reset(data, positions):
    for (y, x) in positions:
        data[y][x] = 0


def inc_surrounding(data, positions):
    for y, x in positions:
        for yi in range(max(y - 1, 0), min(len(data), y + 2)):
            for xi in range(max(x - 1, 0), min(len(data[y]), x + 2)):
                if data[yi][xi] != 0:
                    data[yi][xi] += 1


def step(data):
    flashes = 0
    inc(data)
    while pos := flashing(data):
        reset(data, pos)
        inc_surrounding(data, pos)
        flashes += len(pos)
    return flashes


def synced(data):
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != 0:
                return False
    return True


def part1(data, rounds):
    return sum(step(data) for _ in range(rounds))


def part2(data):
    round = 0
    while not synced(data):
        round += 1
        step(data)
    return round


def main():
    data = [list(map(int, line.rstrip())) for line in fileinput.input()]
    print(part1(deepcopy(data), 100))
    print(part2(deepcopy(data)))


main()
