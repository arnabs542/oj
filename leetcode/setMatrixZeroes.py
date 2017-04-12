#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
73. Set Matrix Zeroes

Total Accepted: 92591
Total Submissions: 262073
Difficulty: Medium
Contributors: Admin

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
==============================================================================================
SOLUTION

Difficulty:
    there are two states for element zeroes: originally 0 or modified to 0.
To differentiate it, we can mark those cell to be set to 0 as a special cell.

1. Naive solution
Set up an auxiliary matrix of the same size storing mutated zeroes.
Scan the matrix, for each value matrix[i][j], if matrix[i][j] is 0, mark auxiliary matrix'
corresponding cell 0.
Then modify the original matrix while checking whether each cell is zero in auxiliary matrix.

Complexity: O((m + n) * #zeroes), O(mn).

2. Mark entire rows and columns
In a another perspective, mark entire rows and columns instead of cells.
Use two auxiliary arrays, indicating where a whole row or column is all zeroes.
Time complexity: O(mn), space complexity: O(m + n).

3. Storing states in place
Storing the previous states in the original matrix: use the first row and column!

'''

class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        return self.setZeroesInplace(matrix)

    def setZeroesInplace(self, matrix):
        if not matrix or not matrix[0]:
            return
        # mark the first column
        col0 = 1 # initialization: not setting zeroes
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col0 = 0
                break
        # mark the rest columns and rows, skipping the first column
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # set zeroes for non-first rows and columns
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = matrix[i][0] and matrix[0][j] and matrix[i][j]

        # set zeroes for first row and column
        if not matrix[0][0]:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if not col0:
            for i in range(len(matrix)):
                matrix[i][0] = 0

    # TODO: some optimization and simplification?

def test():
    solution = Solution()

    matrix = []
    solution.setZeroes(matrix)
    assert matrix == []

    matrix = [[]]
    solution.setZeroes(matrix)
    assert matrix == [[]]

    matrix = [[1]]
    solution.setZeroes(matrix)
    assert matrix == [[1]]

    matrix = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1],
    ]
    solution.setZeroes(matrix)
    print(matrix)
    assert matrix == [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
    ]

    print("self test passed")

if __name__ == '__main__':
    test()
