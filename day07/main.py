#!/usr/bin/env python3
import fileinput
from statistics import median


def fuel(x):
    return (x * (x + 1)) // 2


def part1(data):
    cheapest = int(median(data))
    return sum(abs(x - cheapest) for x in data)


def part2(data):
    fuels = [
        sum(fuel(abs(crab - pos)) for crab in data)
        for pos in range(min(data), max(data))
    ]
    return min(fuels)


def main():
    data = list(map(int, [num for num in fileinput.input().readline().split(",")]))
    print(part1(data))
    print(part2(data))


main()
