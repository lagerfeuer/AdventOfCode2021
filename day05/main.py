#!/usr/bin/env python3
import fileinput
from collections import namedtuple, defaultdict

Point = namedtuple("Point", "x y")


def solve(data, f=None):
    vents = defaultdict(int)
    for (p1, p2) in data:
        if f and f(p1, p2):
            continue
        (x1, y1), (x2, y2) = p1, p2
        xdiff = x2 - x1
        ydiff = y2 - y1
        length = max(abs(xdiff), abs(ydiff))
        xstep = xdiff // length
        ystep = ydiff // length

        for idx in range(length + 1):
            vents[(x1 + idx * xstep, y1 + idx * ystep)] += 1

    return len(list(filter(lambda item: item[1] >= 2, vents.items())))


def main():
    raw = [line.rstrip().split(" -> ") for line in fileinput.input()]
    data = [[Point(*map(int, p.split(","))) for p in pts] for pts in raw]
    print(solve(data, lambda p1, p2: p1.x != p2.x and p1.y != p2.y))
    print(solve(data))


main()
