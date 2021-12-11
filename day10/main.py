#!/usr/bin/env python3
import fileinput
from functools import reduce

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def check(line):
    stack = []
    for char in line:
        if char in pairs.keys():
            stack.append(char)
        else:
            if pairs[stack[-1]] == char:
                stack.pop()
            else:
                return char
    return stack


def autocomplete(stack):
    return [pairs[stack.pop()] for _ in range(len(stack))]


def part1(data):
    tbl = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    return sum(
        tbl[e] for e in filter(lambda e: len(e) == 1, [check(line) for line in data])
    )


def part2(data):
    tbl = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    results = [
        autocomplete(stack)
        for stack in filter(lambda e: len(e) > 1, [check(line) for line in data])
    ]
    scores = [reduce(lambda acc, e: acc * 5 + tbl[e], stack, 0) for stack in results]
    return sorted(scores)[len(scores) // 2]


def main():
    data = [line.rstrip() for line in fileinput.input()]
    print(part1(data))
    print(part2(data))


main()
