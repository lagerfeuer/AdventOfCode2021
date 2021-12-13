#!/usr/bin/env python3
import fileinput


def pprint(points):
    max_x = max(p[0] for p in points) + 1
    max_y = max(p[1] for p in points) + 1
    return "\n".join(
        [
            "".join("#" if (x, y) in points else " " for x in range(max_x))
            for y in range(max_y)
        ]
    )


def fold(points, axis, idx):
    if axis == "y":
        check = lambda p: p[1] > idx
        new_point = lambda p: (p[0], idx - (p[1] - idx))
    else:
        check = lambda p: p[0] > idx
        new_point = lambda p: (idx - (p[0] - idx), p[1])

    result = list(filter(lambda p: not check(p), points))
    for point in filter(check, points):
        p = new_point(point)
        if p not in result:
            result.append(p)
    return result


def solve(points, folds, once=False):
    for (axis, idx) in folds:
        points = fold(points, axis, idx)
        if once:
            return len(points)
    return pprint(points)


def main():
    data = [line.rstrip() for line in fileinput.input()]
    divider = data.index("")
    points = [tuple(map(int, coord.split(","))) for coord in data[:divider]]
    folds = [
        tuple([axis, int(val)])
        for line in data[divider + 1 :]
        for (axis, val) in [line.split()[-1].split("=")]
    ]
    print(solve(points, folds, True))
    print(solve(points, folds))


main()
