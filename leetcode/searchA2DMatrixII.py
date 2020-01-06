#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
240. Search a 2D Matrix II

Total Accepted: 60713
Total Submissions: 160318
Difficulty: Medium
Contributors: Admin

Write an efficient algorithm that searches for a value in an m x n matrix. This
matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


================================================================================
SOLUTION

1. Brute force, O(mn)

2. Heap - top left perspective
Inspecting the matrix from top left angle, it's a heap data structure.

Time complexity O(min(mn, k))

3. Binary Search in each row
Exhaust all rows, the binary search in each row.

Complexity:  O(MlogN)

4. Binary search in 2 dimension
Shrink the search space by two.
The problem is how to divide the space, so that the subspaces are separated evenly.

To divide the space into two equal area regions, we have mathematical equation.
We need to find such anchor point (x, y), instead of the middle point, that
divides the search space evenly,
x * y = ½ mn, x / y = m / n = r.
So, y^2 * r = ½ n^2 r, => y = √2/2 n.

Complexity: O(log(mn))

5. Binary search tree - bottom left perspective - linear solution.

Treat this special matrix as a variant of BINARY SEARCH TREE with two roots:
bottom left and top right.

Then we can search the binary search tree from a very root and eliminate a row
or column depending on the comparison result between the root value and target.

Complexity: O(max(m, n))

================================================================================
FOLLOW UP

1. Find k smallest number
View it as min heap, and maintain a heap?

'''

class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        return self.searchMatrixBinarySearchTree(matrix, target)

    def searchMatrixBinarySearchTree(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True
        return False

def test():
    solution = Solution()

    assert not solution.searchMatrix([], 4)

    assert solution.searchMatrix([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5)
    assert not solution.searchMatrix([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20)

    print("self test passed")

if __name__ == '__main__':
    test()
