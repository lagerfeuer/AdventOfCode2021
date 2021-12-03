#!/usr/bin/env python3
import fileinput


def part1(instructions):
    horizontal = sum(op[1] for op in instructions if op[0] == "forward")
    depth = sum(
        op[1] if op[0] == "down" else -op[1]
        for op in filter(lambda e: e[0] != "forward", instructions)
    )
    return horizontal * depth


def part2(instructions):
    aim = 0
    horizontal = 0
    depth = 0
    for op, value in instructions:
        if op == "forward":
            horizontal += value
            depth += value * aim
        elif op == "up":
            aim -= value
        elif op == "down":
            aim += value
    return horizontal * depth


def main():
    lst = [
        (op, int(value)) for line in fileinput.input() for op, value in [line.split()]
    ]
    print(part1(lst))
    print(part2(lst))


main()
