#!/usr/bin/env python3
import fileinput
from collections import defaultdict, deque, Counter


def part1(graph, start="start", end="end"):
    queue = deque([(start, [start])])
    paths = []
    while queue:
        (curr, path) = queue.popleft()
        if curr == end:
            paths.append(path)
            continue
        seen = set(path)
        for node in graph[curr]:
            if node.isupper() or node not in seen:
                queue.append((node, path + [node]))
    return len(paths)


def part2(graph, start="start", end="end"):
    queue = deque([(start, [start], False)])
    paths = []
    while queue:
        (curr, path, used) = queue.popleft()
        if curr == end:
            paths.append(path)
            continue
        seen = set(path)
        for node in graph[curr]:
            if node == start:
                continue
            if node.isupper() or node not in seen or not used:
                queue.append(
                    (node, path + [node], used or (node.islower() and node in seen))
                )
    return len(paths)


def main():
    edges = [tuple(line.rstrip().split("-")) for line in fileinput.input()]
    connections = defaultdict(list)
    for (a, b) in edges:
        connections[a].append(b)
        connections[b].append(a)
    print(part1(connections))
    print(part2(connections))


main()
