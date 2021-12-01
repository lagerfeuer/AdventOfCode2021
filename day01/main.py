#!/usr/bin/env python3
import fileinput


def part1(lst):
    return sum([y > x for x, y in zip(lst[:-1], lst[1:])])


def part2(lst, n=3):
    sliding_window_lst = [sum(lst[idx : idx + n]) for idx in range(len(lst) - (n - 1))]
    return part1(sliding_window_lst)


def main():
    lst = [int(line) for line in fileinput.input()]
    print(part1(lst))
    print(part2(lst))


main()
