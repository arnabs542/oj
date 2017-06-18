#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
36. Valid Sudoku

Total Accepted: 115216
Total Submissions: 329499
Difficulty: Medium
Contributor: LeetCode

Determine if a Sudoku is valid, according to: [Sudoku Puzzles - The Rules](http://sudoku.com.au/TheRules.aspx).

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


[image](partially filled sudoku.svg.png)
A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells
need to be validated.

==============================================================================================
SOLUTION

Validity of soduku is only affected by three variables: whether there is duplicate in row, column
and sub-box.

1. Use hash table to mark existence.

2. Use array as associative array directly!

'''

class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # return self.isValidSudokuHash(board)
        return self.isValidSudokuArray(board)

    def isValidSudokuHash(self, board):
        n = len(board)
        cols, rows = [set() for _ in range(n)], [set() for _ in range(n)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(n):
            for j, d in enumerate(board[i]):
                if d == '.': continue
                if d in cols[j] or d in rows[i] or d in boxes[i//3][j//3]:
                    return False
                rows[i].add(d)
                cols[j].add(d)
                boxes[i//3][j//3].add(d)
        return True

    def isValidSudokuArray(self, board):
        '''
        Using array as hash table, array's indices as keys, values as hash table's values.
        '''
        n = len(board)
        cols = [[0 for _ in range(n)] for _ in range(n)]
        rows = [[0 for _ in range(n)] for _ in range(n)]
        boxes = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j, c in enumerate(board[i]):
                if c == '.': continue
                d = int(c) - 1
                if cols[j][d] or rows[i][d] or boxes[3 * (i//3) + j//3][d]: return False
                cols[j][d] = rows[i][d] = boxes[3 * (i//3) + j//3][d] = 1
        return True

def test():
    solution = Solution()

    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    assert solution.isValidSudoku(board)

    board = [".87654321","2.8......","3........","4........","5........","6........","7........","8........","9........"]
    assert not solution.isValidSudoku(board)

    print("self test passed")

if __name__ == '__main__':
    test()
