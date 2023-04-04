#!/usr/bin/python3

"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""


import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True


def solve_nqueens(board, col, N):
    """
    Use backtracking to find all solutions
    """
    # Base case: If all queens are placed, print the solution
    if col == N:
        queens_pos = [[i, board[i].index(1)] for i in range(N)]
        print(queens_pos)
        return True
    # Recursive case
    res = False
    for row in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            res = solve_nqueens(board, col + 1, N) or res
            board[row][col] = 0  # backtrack
    return res


if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize empty board
    board = [[0 for x in range(N)] for y in range(N)]

    # Solve and print all solutions
    solve_nqueens(board, 0, N)
