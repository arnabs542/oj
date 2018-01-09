#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
37. Sudoku Solver
Hard


Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

================================================================================
SOLUTION

1. Depth first search

Vertices set is the collection of matrix state.
Edges are valid numbers filling a cell in the matrix.

Define state as a tuple of cell coordinates in the matrix: (i, j)


"""

class Solution:

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        result = self._solveSudokuDfs(board)

        print('solution: ')
        for row in board:
            print(row)

        return result

    def _solveSudokuDfs(self, board):
        n = len(board)
        # visited state
        rows = [[0 for _ in range(n)] for _ in range(n)]
        cols = [[0 for _ in range(n)] for _ in range(n)]
        boxes = [[0 for _ in range(n)] for _ in range(n)]

        def isValid(x, y, num):
            d = num - 1
            if not (0 <= d <= 8 and 0 <= x <= 8): print("ERROR! ", x, y, num, d)
            return not (rows[x][d] or cols[y][d] or boxes[(x // 3) * 3 + y // 3][d])

        def visit(x, y, num, visited=True):
            d = num - 1
            rows[x][d] = visited
            cols[y][d] = visited
            boxes[(x // 3) * 3 + y // 3][d] = visited

        _next = lambda x, y: (x, y + 1) if y < n - 1 else (x + 1, 0)  # next neighbour

        def dfs(x, y):
            while x < n and board[x][y] != '.':
                x, y = _next(x, y)
            if x >= n:
                return True  # base case

            for i in range(1, n + 1):
                if not isValid(x, y, i):
                    continue
                board[x][y] = str(i)
                visit(x, y, i)
                if dfs(*_next(x, y)):
                    return True  # recursive to next neighbour
                visit(x, y, i, False)  # backtrack: restore state
                board[x][y] = '.'
            return False

        # initialize state
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    visit(i, j, int(board[i][j]))
        return dfs(0, 0)


def test():
    solution = Solution()

    board = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."],
    ]
    assert solution.solveSudoku(board)

    assert board == [
        ["5", "1", "9", "7", "4", "8", "6", "3", "2"],
        ["7", "8", "3", "6", "5", "2", "4", "1", "9"],
        ["4", "2", "6", "1", "3", "9", "8", "7", "5"],
        ["3", "5", "7", "9", "8", "6", "2", "4", "1"],
        ["2", "6", "4", "3", "1", "7", "5", "9", "8"],
        ["1", "9", "8", "5", "2", "4", "3", "6", "7"],
        ["9", "7", "5", "8", "6", "3", "1", "2", "4"],
        ["8", "3", "2", "4", "9", "1", "7", "5", "6"],
        ["6", "4", "1", "2", "7", "5", "9", "8", "3"],
    ]
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    assert solution.solveSudoku(board)

    board = [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    assert solution.solveSudoku(board)

    print("self test passed!")

if __name__ == '__main__':
    test()
