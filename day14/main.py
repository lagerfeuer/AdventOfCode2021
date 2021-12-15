#!/usr/bin/env python3
import fileinput
from collections import defaultdict


def prepare(seq):
    pairs = defaultdict(int)
    freq = defaultdict(int)
    for idx in range(len(seq) - 1):
        pairs[seq[idx : idx + 2]] += 1
        freq[seq[idx]] += 1
    freq[seq[-1]] += 1
    return pairs, freq


def solve(pairs, freq, rules, iterations=1):
    for _ in range(iterations):
        for (pair, cnt) in list(pairs.items()):
            if pair in rules:
                pairs[pair] -= cnt
                pairs[pair[0] + rules[pair]] += cnt
                pairs[rules[pair] + pair[1]] += cnt
                freq[rules[pair]] += cnt
    return max(freq.values()) - min(freq.values())


def main():
    data = [line.rstrip() for line in fileinput.input()]
    rules = {l: r for rule in data[2:] for l, r in [rule.split(" -> ")]}
    pairs, freq = prepare(data[0])
    print(solve(pairs, freq, rules, iterations=10))
    print(solve(pairs, freq, rules, iterations=30))


main()
