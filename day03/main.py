#!/usr/bin/env python3
import fileinput
from operator import le, gt
from copy import copy


def freq(data, idx):
    bits = [e[idx] for e in data]
    return (bits.count("0"), bits.count("1"))


def to_freq(data):
    for idx in range(len(data[0])):
        yield freq(data, idx)


def rating(data, f):
    prefix = ""
    filtered = copy(data)
    while len(filtered) > 1:
        (zeros, ones) = freq(filtered, len(prefix))
        prefix += "0" if f(zeros, ones) else "1"
        filtered = list(filter(lambda e: e.startswith(prefix), data))
    return int(filtered.pop(), 2)


def part1(data):
    gamma = "".join([str(int(zeros < ones)) for (zeros, ones) in to_freq(data)])
    epsilon = gamma.translate(gamma.maketrans("01", "10"))
    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    return rating(data, gt) * rating(data, le)


def main():
    data = [line.rstrip() for line in fileinput.input()]
    print(part1(data))
    print(part2(data))


main()
