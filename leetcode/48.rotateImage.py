#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
48. Rotate Image

Total Accepted: 99511
Total Submissions: 265833
Difficulty: Medium
Contributors: Admin

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

================================================================================
SOLUTION

--------------------------------------------------------------------------------
LINEAR TRANSFORMATION explained with LINEAR ALGEBRA and TRIANGLE IDENTITIES

This is a linear transformation in linear algebra problem. And the transformation matrix is
about to rotate by 90 degrees (clockwise).

Denote the original point by P(x, y), and point obtained by applying transformation matrix A
is P'(x',y').

Then we have:
    x' = r\cos(α + β)
    y' = r\sin(α + β)
where (r, β) is the polar coordinate representation of P(x, y). And  is the rotation angle.

Let β=-π/2, and
x' = r\sin(α) = y
y' = -r\cos(α) = -x

--------------------------------------------------------------------------------
Thus the transformation can be expressed with transformation matrix:
    A = [
        [cosβ, -sinβ],
        [sinβ, cosβ],
    ]
Let β=-π/2, and then:
    A = [
    [0, 1],
    [-1, 0]
    ]
P' = AP => (x', y') = (y, -x)

--------------------------------------------------------------------------------
1. Brute force - with extra space
Use extra space to cache, transform using the above coordinate transform relation.

Complexity:O(N²), O(N²)

2. Combined transformation of transpose, reflection.
Basic transformations that can be done inplace: translate, reflect, transpose.

Transpose transform matrix is:
    A = [
    [0, 1],
    [1, 0]
    ]
Reflect around x asix:
    A = [
    [1, 0],
    [0, -1]
    ]
Reflect around y asix:
    A = [
    [-1, 0],
    [0, 1]
    ]

An intuition is that, after transformation by rotating by clockwise 90 degrees,
(y, x) => (y, -x), where x and y are swapped, and there is a reflection of of a coordinate.

This suggests that the transformation could be combined from two successive individual
transformation: transpose, and reflect around x axis.

Mathematical proof by transformation matrix multiplication is followed:
A(rotate by 90 degrees, clockwise) = A(Reflect around x asix) * A(Transpose transform matrix)

Which means, we can first transpose, and then reflect around x axis. And also, it's equivalent
to reflect around y axis, then transpose.

Complexity: O(N²), O(1)

3. Layer-wise rotating
(from http://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/)
An N x N matrix will have floor(N/2) SQUARE CYCLES.
For example, a 4 X 4 matrix will have 2 cycles. The first cycle is formed by its 1st row,
last column, last row and 1st column. The second cycle is formed by 2nd row, second-last column,
second-last row and 2nd column.

The idea is for each square cycle, we swap the elements involved with the corresponding cell in
the matrix in anti-clockwise direction i.e. from top to left, left to bottom, bottom to right and
from right to top one at a time. We use nothing but a temporary variable to achieve this.

First Cycle
 1     2  3 4
   ---------
 5 |   6  7| 8
 9 |  10 11|12
   ---------
 13|  14 15|16

For each square cycle, there are 4(m-1) numbers, where m is the side length of the square.
And the coordinates of four points are:
    top left=(x, x)
    top right=(x, n - 1 - (x - 0)) = (x, n - x - 1)
    bottom right =(n - x - 1, n - x - 1)
    bottom left = (n - x - 1, x)

For each point on one side, there are three other corresponding points with respect to current
rotation.
For a number at the top side (x, y), its corresponding points in this rotation cycle are:
    (x, y),
    (x + y - x, n - 1 - x) = (y, n - 1 - x),
    (n - x - 1, n - 1 - x - (y - x)) = (n - x - 1, n - y - 1),
    (n - 1 - x - (y - x), x) = (n - y - 1, x)
where y is in range [x, n - 1 - x - 1] = [x, n - x - 2]

'''

class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # self._rotateTransposeAndReflect(matrix)
        self._rotateCyclewise(matrix)

    def _rotateTransposeAndReflect(self, matrix: list):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def _rotateCyclewise(self, matrix: list):
        n = len(matrix)
        for x in range(n//2): # each square cycle
            for y in range(x, n - x - 1): # 4(m -1), m = n - 2i
                a = matrix[x][y]
                matrix[x][y] = matrix[n - 1 - y][x]
                matrix[n - 1 - y][x] = matrix[n - x - 1][n - 1 -y]
                matrix[n - x - 1][n - 1 - y] = matrix[y][n - 1 - x]
                matrix[y][n - 1 - x] = a
        pass

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
