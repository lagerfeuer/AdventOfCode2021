#!/usr/bin/env python3
import fileinput


def solve(data, days):
    fishes = [data.count(idx) for idx in range(9)]
    for _ in range(days):
        tmp = fishes[0]
        for idx in range(len(fishes) - 1):
            fishes[idx] = fishes[idx + 1]
        fishes[len(fishes) - 1] = tmp
        fishes[6] += tmp
    return sum(fishes)


def main():
    data = list(map(int, fileinput.input().readline().split(",")))
    print(solve(data, 80))
    print(solve(data, 256))


main()
