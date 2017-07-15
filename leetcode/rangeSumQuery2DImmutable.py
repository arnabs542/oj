#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by
its upper left corner (row0, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and
(row1, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
  - You may assume that the matrix does not change.
  - There are many calls to sumRegion function.
  - You may assume that row1 ≤ row2 and col1 ≤ col2.

==============================================================================================
SOLUTION

1. Brute force

Complexity: O(mn)

2. Cache matrix result

Complexity: O(1) query, O(M²N²) initialization, O(M²N²) space

3. Cache rows
Use 1D prefix sum and accumulate row by row for query.
Complexity: O(m) query, O(mn) initialization, O(mn) space

4. 2D prefix sum(integation)

Like the 1D case, we can still build the prefix sum. And the only difference is that now it's
2D.

By observing the geometric rectangle region, we can use the principle inclusion-exclusion to
calculate of a rectangle region.

Denote the function prefix sum as f, then f[x][y] is the sum over elements from (0, 0) to (x, y).
So we have such equation:

sumRegion(row1, col1, row2, col2)
= f[row2][col2] - f[row2][col2 - 1] - f[row1][col + 1] + f[row1][col1]

'''

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self._matrix = matrix
        self._buildPrefixSum()

    def _buildPrefixSum(self):
        if not self._matrix or not self._matrix[0]:
            self._prefixSum = None
            return
        prefixSum = [[0 for _ in range(len(self._matrix[0]) + 1)]
                     for _ in range(len(self._matrix) + 1)]
        for i in range(1, len(self._matrix) + 1):
            for j in range(1, len(self._matrix[0]) + 1):
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - \
                    prefixSum[i - 1][j - 1] + self._matrix[i - 1][j - 1]
        self._prefixSum = prefixSum

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ps = self._prefixSum
        value = ps[row2 + 1][col2 + 1] - ps[row2 + 1][col1] - \
            ps[row1][col2 + 1] + ps[row1][col1]
        # print('values: ', ps[row2 + 1][col2 + 1], ps[row2 + 1][col1],
              # ps[row1][col2 + 1], ps[row1][col1], value)
        return value


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

def test():
    import numpy as np
    from pprint import pprint as print

    obj = NumMatrix([])
    # assert obj.sumRegion(0, 0, 0, 0) == 0

    # case
    obj = NumMatrix([[1]])
    assert obj.sumRegion(0, 0, 0, 0) == 1

    obj = NumMatrix([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ])

    assert obj._prefixSum[-1][-1] == np.sum(obj._matrix)

    assert obj.sumRegion(0, 0, 4, 4) == 58
    assert obj.sumRegion(0, 0, 4, 1) == 23
    assert obj.sumRegion(2, 1, 4, 3) == 8
    assert obj.sumRegion(1, 1, 2, 2) == 11
    assert obj.sumRegion(1, 2, 2, 4) == 12
    assert obj.sumRegion(2, 2, 0, 0) == 6
    assert obj.sumRegion(0, 0, 2, 2) == 21

    # case
    obj = NumMatrix([[3, 0, 1, 4, 2]])

    print('prefix sum: ')
    print(obj._prefixSum)
    assert obj.sumRegion(0, 0, 0, 3) == 8
    assert obj.sumRegion(0, 0, 0, 2) == 4
    assert obj.sumRegion(0, 0, 0, 1) == 3
    assert obj.sumRegion(0, 0, 0, 0) == 3

    # case
    obj = NumMatrix([[3], [0], [1], [4], [2]])

    print('prefix sum: ')
    print(obj._prefixSum)
    assert obj.sumRegion(0, 0, 3, 0) == 8
    assert obj.sumRegion(0, 0, 2, 0) == 4
    assert obj.sumRegion(0, 0, 1, 0) == 3
    assert obj.sumRegion(0, 0, 0, 0) == 3

    print('self test passed')

if __name__ == '__main__':
    test()
