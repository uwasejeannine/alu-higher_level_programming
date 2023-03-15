#!/usr/bin/env python3
import sys

def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_valid(board, row, col):
        for r, c in board:
            if c == col or r - c == row - col or r + c == row + col:
                return False
        return True

    def solve(board, row):
        if row == n:
            print(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                solve(board + [(row, col)], row + 1)

    solve([], 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(n)
