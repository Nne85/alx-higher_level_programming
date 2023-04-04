#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, col, N, solutions):
    if col == N:
        queens = []
        for row in range(N):
            for col in range(N):
                if board[row][col]:
                    queens.append([row, col])
        solutions.append(queens)
        return
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens(board, col + 1, N, solutions)
            board[row][col] = 0

def n_queens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0 for i in range(N)] for j in range(N)]
    solutions = []
    solve_n_queens(board, 0, N, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    n_queens(N)
