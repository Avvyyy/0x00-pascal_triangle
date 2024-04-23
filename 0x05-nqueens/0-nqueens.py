#!/usr/bin/python3
"""
nqueens.py: Solve the N queens problem and print all possible solutions.

Usage: nqueens N

If the user called the program with the wrong number of arguments, print:
    Usage: nqueens N
    followed by a new line, and exit with the status 1,
where N must be an integer greater or equal to 4.

If N is not an integer, print:
    N must be a number
    followed by a new line, and exit with the status 1.

If N is smaller than 4, print:
    N must be at least 4
    followed by a new line, and exit with the status 1.

The program prints every possible solution to the problem, one solution per line.
"""

import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen in the given position."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N, result):
    """Utility function to solve the N queens problem recursively."""
    # Base case: If all queens are placed, then append the result
    if col >= N:
        result.append([[row, col] for row in range(N) if board[row][col - 1] == 1])
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_n_queens_util(board, col + 1, N, result)

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0

def solve_n_queens(N):
    """Solve the N queens problem and print all possible solutions."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)

    for sol in result:
        print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
