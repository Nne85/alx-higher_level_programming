#!/usr/bin/python3

"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


import sys


def is_safe(board, row, col):
    # Check if the given position is safe for a queen
    n = len(board)
    # Check the row
    for j in range(col):
        if board[row][j] == 1:
            return False
    # Check the upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check the lower diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def nqueens(board, col, solutions):
    n = len(board)
    if col == n:
        # We have placed all the queens, save the solution
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for row in range(n):
        if is_safe(board, row, col):
            # Place the queen
            board[row][col] = 1
            # Try to place the next queen
            nqueens(board, col+1, solutions)
            # Backtrack
            board[row][col] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    # Initialize the chessboard
    board = [[0 for j in range(n)] for i in range(n)]
    # Solve the problem
    solutions = []
    nqueens(board, 0, solutions)
    # Print the solutions
    for solution in solutions:
        print(solution)
