#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
63. Unique Paths II

Total Accepted: 85453
Total Submissions: 278199
Difficulty: Medium
Contributors: Admin

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

==============================================================================================
SOLUTION:
    Now we have to count one by one with Dynamic Programming.
'''

class Solution(object):

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        return self.uniquePathsWithObstaclesDP(obstacleGrid)

    def uniquePathsWithObstaclesDP(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        f = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == j == 0:
                    f[i][j] = 1
                f[i][j] += f[i - 1][j] if i else 0
                f[i][j] += f[i][j - 1] if j else 0

        print(f)
        return f[-1][-1]

def test():
    solution = Solution()

    assert solution.uniquePathsWithObstacles([]) == 0

    assert solution.uniquePathsWithObstacles([[1]]) == 0
    assert solution.uniquePathsWithObstacles([[1, 0]]) == 0

    assert solution.uniquePathsWithObstacles([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]) == 2

    print('self test passed')

if __name__ == '__main__':
    test()
