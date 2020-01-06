#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
419. Battleships in a Board

Given an 2D board, count how many battleships are in it. The battleships are represented
with 'X's, empty slots are represented with '.'s. You may assume the following rules:

  You receive a valid board, made of only battleships or empty slots.
  Battleships can only be placed horizontally or vertically. In other words, they can only
be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
  At least one horizontal or vertical cell separates between two battleships - there are no
adjacent battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X

This is an invalid board that you will not receive - as battleships will always have a cell
separating between them.

Follow up:
Could you do it in one-pass, using only O(1) extra memory and without modifying the value of
the board?

==============================================================================================
SOLUTION

Well, we can start by leaving out the follow up constraints to find a naive solution first.

1. Treat it as graph problem, and find the connected components, in with DFS
But to use DFS, auxiliary space are needed to mark node traversal state: to visit, visiting,
and visited.

2. Scan the coordinates
Since the input is always valid, we can easily count distinct battleships.

Scan the board from top down, left to right.
The condition setup is that there are no adjacent ships. Then a slot with 'X' indicates
a new battleship if and only if its visited neighbors, top and left ones, are both not 'X's.

Complexity: O(N), O(1)

'''

from _decorators import timeit


class Solution(object):

    @timeit
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        result = self._countBattleshipsLinearScan(board)
        print(result)
        return result

    def _countBattleshipsDfs(self, board):
        pass

    def _countBattleshipsLinearScan(self, board):
        # if not board or not board[0]: return 0
        n = 0
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if board[i][j] == 'X' \
                   and (i == 0 or board[i-1][j] == '.') \
                   and (j == 0 or board[i][j-1] == '.'):
                    n += 1
        return n

def test():
    """TODO: Docstring for test.
    :returns: TODO

    """

    solution = Solution()

    board = []
    assert solution.countBattleships(board) == 0

    board = [
        [],
        [],
    ]
    assert solution.countBattleships(board) == 0

    board = [
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"],
    ]
    assert solution.countBattleships(board) == 2

    # board = [
        # ['.', '.', '.', 'X'],
        # ['X', 'X', 'X', 'X'],
        # ['.', '.', '.', 'X'],
    # ]
    # assert solution.countBattleships(board) == 2

    print("self test passed")

if __name__ == '__main__':
    test()
