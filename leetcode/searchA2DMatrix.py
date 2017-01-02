#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
74. Search a 2D Matrix

Total Accepted: 105702
Total Submissions: 296778
Difficulty: Medium
Contributors: Admin

Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

==============================================================================================
SOLUTION

Binary search in the index space.

1. Two round binary search dimension by dimension: first search the first dimension, row, then,
search the column dimension.

2. Treat the matrix as a one-dimensional sorted list


'''

class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # return self.searchMatrixBinarySearch(matrix, target)
        return self.searchMatrixBinarySearch1D(matrix, target)

    def searchMatrixBinarySearch(self, matrix, target):
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (high + low) >> 1
            if matrix[mid][0] > target: high = mid - 1
            elif matrix[mid][0] < target: low = mid + 1
            else: return True
        row = high
        if not 0 <= row <= len(matrix) - 1: return False
        low, high = 0, len(matrix[0]) - 1
        while low <= high:
            mid = (high + low) >> 1
            if matrix[row][mid] > target: high = mid - 1
            elif matrix[row][mid] < target: low = mid + 1
            else: return True
        return False

    def searchMatrixBinarySearch1D(self, matrix, target) -> int:
        if not matrix: return False
        low, high = 0, (len(matrix) * len(matrix[0]) - 1)
        while low <= high:
            mid = (low + high) >> 1
            value = matrix[mid // len(matrix[0])][mid % len(matrix[0])]
            if value > target: high = mid - 1
            elif value < target: low = mid + 1
            else: return True
        return False

def test():
    solution = Solution()

    assert solution.searchMatrix([
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50],
    ], 3)

    assert not solution.searchMatrix([], 0)

    print("self test passed")

if __name__ == '__main__':
    test()
