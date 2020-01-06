#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
289. Game of Life Add to List

Total Accepted: 41128
Total Submissions: 112831
Difficulty: Medium
Contributors: Admin

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a
cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each
cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following
four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
1. Could you solve it in-place? Remember that the board needs to be updated at the same time:
    You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite,
which would cause problems when the active area encroaches the border of the array. How would
you address these problems?

==============================================================================================
SOLUTION

1. Naive solution
Use an auxiliary matrix to represent the next states. Complexity: O(mn), O(mn)

2. State encoded with BIT REPRESENTATION
A cell has two states, live or dead. And the state transition is bidirectional, forming
4 different transitions: 0->0, 0->1, 1->0, 1->0. The tuple (current state, next state) has
only 4 values: (0, 0), (0, 1), (1, 0), (1, 1). Then we can represent the tuple with 2 bits!

1) Use the Least Significant Bit to represent the current state, the second LSB as next state.
2) Compute a cell's next state using neighbors' current state, and store it in the second LSB.
3) Eliminate current state, by shifting the state rightward by 1.


'''

class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.gameOfLifeBit(board)

    def gameOfLifeBit(self, board):
        def liveNeighbors(x, y):
            result = 0
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1),
                         (-1, -1), (1, -1), (1, 1), (-1, 1)):
                if not (0 <= x + i < len(board)
                        and 0 <= y + j < len(board[0])):
                    continue
                result += board[x + i][y + j] & 0x1
            return result

        def transite(state0, live):
            '''
            state0: current state
            live: number of live neighbor cells
            returns next state
            '''
            return 1 if state0 == 1 and live in (
                2, 3) or state0 == 0 and live == 3 else 0
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                live = liveNeighbors(i, j)
                state1 = transite(board[i][j], live)
                board[i][j] |= state1 << 1

        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                board[i][j] >>= 1

        print(board)


def test():
    solution = Solution()

    matrix = []
    solution.gameOfLife(matrix)
    assert matrix == []

    matrix = [[]]
    solution.gameOfLife(matrix)
    assert matrix == [[]]

    matrix = [[0, 0, 1],
              [0, 1, 0],
              [0, 1, 0]]
    solution.gameOfLife(matrix)
    assert matrix == [[0, 0, 0],
                      [0, 1, 1],
                      [0, 0, 0]]

    matrix = [[0, 1, 0],
              [0, 1, 0],
              [0, 1, 0]]
    solution.gameOfLife(matrix)
    assert matrix == [[0, 0, 0],
                      [1, 1, 1],
                      [0, 0, 0]]

    matrix = [[0, 0, 0],
              [1, 1, 1],
              [0, 0, 0]]
    solution.gameOfLife(matrix)
    assert matrix == [[0, 1, 0],
                      [0, 1, 0],
                      [0, 1, 0]]

    matrix = [[1, 1, 0],
              [1, 0, 0],
              [0, 0, 0]]
    solution.gameOfLife(matrix)
    assert matrix == [[1, 1, 0],
                      [1, 1, 0],
                      [0, 0, 0]]

    matrix = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]]
    solution.gameOfLife(matrix)
    assert matrix == [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]]

    print("self test passed")

if __name__ == '__main__':
    test()
