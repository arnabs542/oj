#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
85. Maximal Rectangle

Total Accepted: 51809
Total Submissions: 205955
Difficulty: Hard
Contributors: Admin

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing
only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

=========================================================================================
SOLUTION


1. Brute force
Enumerate all possible rectangles, and verify.

A rectangle can be determined by left top and bottom right vertices.
A single vertex has MN possible locations, adding another one make it squared.

To verify it, complexity is O(area of rectangle).

Complexity: O(MNxMNxMN) = O(M³N³)

2. Dynamic Programming - counting as summing - prefix sum

The counting 1s process takes too much complexity, O(MN).

----------------------------------------------------------------------------------------------
COUNT AS A SUMMING PROBLEM

One problem here, is to find whether 1s form a rectangle. In another word, we need to
count how many 1s are there in a rectangle. And, all cells have value between 0 and 1.
So, the number of 1s can be represented by the sum of values...

----------------------------------------------------------------------------------------------
PREFIX SUM

And for range sum query, we have prefix sum, segment tree, binary indexed tree!
Just choose one...

Using prefix sum, the range sum can be obtained in O(1) complexity.

Complexity: O(M²N²)

Optimization? Prune?

3. Dynamic programming without inner loop state transition?

NO CLUE...

Although counting is now O(1), but, of course, duplicate calculations are involved, while
searching for the other vertex on the diagonal axis.

A recurrence relation to eliminate that?
During the iteration, for each point(i, j) with value 1, it can form a rectangle, in such
scenarios:
  1) Starting a new 1x1 rectangle
  2) Extend a previous rectangle from (i - 1, j - 1)
  3) Extend a previous rectangle from (i, j - 1)
  4) Extend a previous rectangle from (i - 1, j)


    Let dp[i][j] be the maximal rectangle's (width, height) of which the bottom-right point
is (i, j) in the matrix. Then we can formulate a RECURSION RELATION(STATE TRANSITION) between
dp[i][j] and dp[i-1][j], dp[i][j-1].
1) Take the overlapping parts as the new rectangle:
    width[i][j] = min(width[i-1][j], width[i][j-1]+1)
    height[i][j] = min(height[i-1][j]+1, height[i][j-1])
2) But how about cases like [[0, 1], [0, 1]]?

4. Stack - similar to largest rectangle in histogram

In the matrix, each column can be thought of a histogram bar.

Yeah, iterate the matrix row by row, column by column. And build a matrix containing
bar height starting at cell matrix[i][j].
While scanning a row from left to right, the problem is reduced to "largest rectangle in histogram".

Maintain a monotonic stack for heights, and starting computing locally optimal values
when a bar with smaller height occurs.

Complexity: O(mn)

'''

from _decorators import timeit

class Solution:
    @timeit
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # result = self._maximalRectangleDpPrefixSum(matrix)
        result = self._maximalRectangleMonotoneStack(matrix)

        print(matrix, 'result: ', result)

        return result

    def _maximalRectangleDpPrefixSum(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        ps = [[0 for _ in range(n + 1)] for _ in range(m + 1)] # prefix sum

        areaMax = 0
        # build prefix sum
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ps[i][j] = ps[i - 1][j] + ps[i][j - 1] - ps[i - 1][j - 1] + int(matrix[i - 1][j - 1])
                if int(matrix[i - 1][j - 1]) == 0: continue
                for k in range(1, i + 1):
                    for l in range(1, j + 1):
                        if int(matrix[k - 1][l - 1]) == 0: continue
                        rangeSum = ps[i][j] - ps[k - 1][j] - ps[i][l - 1] + ps[k - 1][l - 1]
                        if rangeSum == (i - k + 1) * (j - l + 1):
                            areaMax = max(areaMax, rangeSum)
                            break

        return areaMax

    def _maximalRectangleMonotoneStack(self, matrix):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        area = 0
        height = [[int(matrix[i][j]) if j < n else 0 for j in range(n + 1)] for i in range(m)]

        # build bar height matrix
        for i in range(m):
            stack = [] # monotone stack for bar heights
            matrix[i].append('0') # add sentinel
            for j in range(n + 1):
                if matrix[i][j] == '1':
                    height[i][j] = height[i - 1][j] + 1 if i else 1 # only depends on last row, space optimization possible
                while stack and height[i][stack[-1]] > height[i][j]:
                    h = stack.pop()
                    left = stack[-1] + 1 if stack else 0
                    width = j - left
                    area = max(area, width * height[i][h])

                stack.append(j)

        return area


def test():
    solution = Solution()

    matrix = []
    assert solution.maximalRectangle(matrix) == 0

    matrix = [[]]
    assert solution.maximalRectangle(matrix) == 0

    matrix = [["0"]]
    assert solution.maximalRectangle(matrix) == 0

    matrix = [["1"]]
    assert solution.maximalRectangle(matrix) == 1

    matrix = [["0"]]
    matrix = [["1"]]
    assert solution.maximalRectangle(matrix) == 1

    matrix = [["0", "1", "1"]]
    assert solution.maximalRectangle(matrix) == 2

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
    ]
    assert solution.maximalRectangle(matrix) == 3

    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    assert solution.maximalRectangle(matrix) == 6

    # test large data
    import yaml
    with open('./maximalRectangle.json', 'r') as f:
        data = yaml.load(f)

    for c in data:
        assert solution.maximalRectangle(c['input']) == c['output']


    print("self test passed!")


if __name__ == "__main__":
    test()
