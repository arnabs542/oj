#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
48. Rotate Image Add to List

Total Accepted: 99511
Total Submissions: 265833
Difficulty: Medium
Contributors: Admin

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
==============================================================================================
SOLUTION

1. Transpose, reverse each row.

'''

class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        return self.rotateTransposeAndReverse(matrix)

    def rotateTransposeAndReverse(self, matrix: list):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def test():
    solution = Solution()

    matrix = []
    solution.rotate(matrix)
    assert matrix == []

    matrix = [[1, 2], [3, 4]]
    solution.rotate(matrix)
    assert matrix == [[3, 1], [4, 2]]

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution.rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    print("self test passed")

if __name__ == '__main__':
    test()
