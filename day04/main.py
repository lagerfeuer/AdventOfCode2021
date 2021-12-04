#!/usr/bin/env python3
import fileinput

SIZE = 5


class Board:
    def __init__(self, data):
        self.board = [[int(e) for e in row.split()] for row in data]
        self.checked = [[False for _ in range(SIZE)] for _ in range(SIZE)]
        self.nums = set([e for sublist in self.board for e in sublist])

    def is_winner(self):
        for row in self.checked:
            if sum(row) == len(row):
                return True
        for idx in range(SIZE):
            col = [row[idx] for row in self.checked]
            if sum(col) == len(col):
                return True
        return False

    def mark(self, num):
        for ri, row in enumerate(self.board):
            try:
                ci = row.index(num)
                self.checked[ri][ci] = True
                self.nums.remove(num)
            except:
                pass

    def unmarked(self):
        return list(self.nums)


def part1(draws, boards):
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.is_winner():
                return sum(board.unmarked()) * draw


def part2(draws, boards):
    for draw in draws:
        before = []
        after = []
        for board in boards:
            before.append(board.is_winner())
            board.mark(draw)
            after.append(board.is_winner())
        if all(after):
            return sum(boards[before.index(False)].unmarked()) * draw


def main():
    data = [line.rstrip() for line in fileinput.input()]
    draws = [int(e) for e in data[0].rstrip().split(",")]
    boards_data = [data[idx : idx + SIZE] for idx in range(2, len(data), SIZE + 1)]
    boards = [Board(data) for data in boards_data]

    print(part1(draws, boards))
    print(part2(draws, boards))


main()
