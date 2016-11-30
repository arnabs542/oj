#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
62. Unique Paths

Total Accepted: 114274
Total Submissions: 294258
Difficulty: Medium
Contributors: Admin

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

==============================================================================================
SOLUTION:
    Combinatoric problem.

Recurrence relation:
    f[m][n] = f[m-1][n] + f[m][n-1]

1. Dynamic Programming

2. Derivate the CLOSE-FORM solution from the RECURRENCE RELATION
For a m x n grid, there are total (m - 1 + n - 1) steps to take: m - 1 steps downwards, n -1
rightwards. Different combinations of rightward and downward steps gives different paths. Then
the problem is reduced to "Given (m - 1 + n - 1), choose (m - 1) unique numbers", meaning first
choose where to take downward steps, then the rest will be rightward steps for sure, which is
the combinatorial number of (m - 1) given (m - 1 + n - 1).

'''

import math

class Solution(object):

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # return self.uniquePathsDP(m, n)
        return self.uniquePathsCombinatoric(m, n)

    def uniquePathsDP(self, m: int, n: int) -> int:
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m * n:
            return 0
        dp = [[0 if i * j else 1 for j in range(n)] for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp)
        return dp[m - 1][n - 1]

    def uniquePathsCombinatoric(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // \
                math.factorial(m - 1) // math.factorial(n - 1) if m * n else 0

def test():
    solution = Solution()

    assert solution.uniquePaths(0, 0) == 0
    assert solution.uniquePaths(1, 2) == 1
    assert solution.uniquePaths(1, 10) == 1
    assert solution.uniquePaths(3, 7) == 28
    print('self test passed')

if __name__ == '__main__':
    test()
