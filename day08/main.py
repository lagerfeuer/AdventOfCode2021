#!/usr/bin/env python3
import fileinput


def find(iterable, pred):
    return next(filter(pred, iterable), None)


def length(l):
    return lambda s: len(s) == l


def strsort(str):
    return "".join(sorted(str))


def get_mapping(pattern):
    mapping = {
        1: find(pattern, length(2)),
        4: find(pattern, length(4)),
        7: find(pattern, length(3)),
        8: find(pattern, length(7)),
    }
    mapping[9] = find(
        pattern, lambda x: len(x) == 6 and set(x).issuperset(set(mapping[4]))
    )
    mapping[0] = find(
        pattern,
        lambda x: len(x) == 6
        and set(x).issuperset(set(mapping[7]))
        and x not in mapping.values(),
    )
    mapping[3] = find(
        pattern,
        lambda x: len(x) == 5
        and len(set(x).intersection(set(mapping[7]))) == 3
        and x not in mapping.values(),
    )
    mapping[6] = find(
        pattern,
        lambda x: len(x) == 6
        and len(set(x).intersection(set(mapping[0]))) == 5
        and x not in mapping.values(),
    )
    mapping[5] = find(
        pattern,
        lambda x: len(x) == 5
        and len(set(x).intersection(set(mapping[9]))) == 5
        and x not in mapping.values(),
    )
    mapping[2] = find(pattern, lambda x: x not in mapping.values())
    return {strsort(v): k for k, v in mapping.items()}


def part1(data):
    unique = set([2, 3, 4, 7])
    return sum(len(digit) in unique for (_, output) in data for digit in output)


def part2(data):
    result = []
    for (pattern, output) in data:
        mapping = get_mapping(pattern)
        result.append(
            sum(
                mapping[strsort(val)] * pow(10, idx)
                for idx, val in enumerate(reversed(output))
            )
        )
    return sum(result)


def main():
    data = [
        tuple(part.split() for part in line.split("|")) for line in fileinput.input()
    ]
    print(part1(data))
    print(part2(data))


main()
