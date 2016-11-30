#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
64. Minimum Path Sum

Total Accepted: 92895
Total Submissions: 251560
Difficulty: Medium
Contributors: Admin

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom
right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.minPathSumDP(grid)

    def minPathSumDP(self, grid: list) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = grid[i][j] + (min(
                    dp[i - 1][j] if i else 1 << 31,
                    dp[i][j - 1] if j else 1 << 31)
                    if i + j > 0 else 0)
                pass

        print(dp)
        return dp[-1][-1]

    # TODO: reduce space complexity to O(n) in dynamic programming

def test():
    solution = Solution()

    assert solution.minPathSumDP([]) == 0
    assert solution.minPathSumDP([[0]]) == 0
    assert solution.minPathSumDP([[2, 3, 1]]) == 6
    print('self test passed')

if __name__ == '__main__':
    test()
