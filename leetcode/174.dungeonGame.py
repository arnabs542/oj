#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
174. Dungeon Game

Total Accepted: 30836
Total Submissions: 137709
Difficulty: Hard
Contributors: Admin

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of
a dungeon.
The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially
positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his
health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon
entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the
knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward
or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the
princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he
follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

    |-2 (K) |-3     |3      |
    |-5     |-10    |1      |
    |10     |30     |-5 (P) |

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the
bottom-right room where the princess is imprisoned.

=================================================================================================
Complexity ANALYSIS:
    Total number of paths.
    This is a M x N matrix, to move from top-left to bottom-right, we have P = (M - 1 + N - 1)
steps to take. And each step is either rightward or downward, which means there is no difference
of path if we exchange two steps towards to the same direction. And if we choose at which time to
move rightward, then we'll have to move downward at the rest of steps. So the total number of all
possible paths is a mathematical combination of
    `\mathcal{C}_n^{m}`, where `n = P`, `m = M - 1`, similar to Catalan Number.

==============================================================================================
SOLUTION:
    1. Brute force breadth-first or depth-first search on the matrix(graph),
combination(C_{m+n}^n) time complexity.

    2. Dynamic Programming.

        1) Try:dp[i][j] denotes a minimal required hp, optimal path to cell[i][j]. Then the
recursive formula would consider many cases because the current cell may reduce the hp, so the
minimal requirement would depend on the final hp before the knight arrives at cell[i][j]. If we
store all these states in dp[i][j], then the time complexity still goes up because different
scenarios are adding up in a Fibonacci sequence way if we don't filter to prune.

        2) BACKWARD INDUCTION
If we reason backwards in time, from the end of a situation, and let hp[i][j] denote the minimal
hp requirement to get to matrix[i][j], then the can have straight relation with hp[i+1][j] and
hp[i][j+1]. Then the state transition recursive formula would be of complexity of O(1).
O(mn) time, O(mn) space.
'''

class Solution(object):

    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # return self.calculateMinimumHPDP(dungeon)
        return self.calculateMinimumHPDPSlidingArray(dungeon)

    def calculateMinimumHPDP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m, n = len(dungeon), len(dungeon[0])
        hp = [[1 << 31] * (n + 1) for i in range(m + 1)]
        # dummy variables to make it clean
        hp[m][n - 1] = hp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                hp[i][j] = min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j]
                hp[i][j] = max(1, hp[i][j])
                pass
        print(hp)
        return hp[0][0]

    def calculateMinimumHPDPSlidingArray(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int

        Optimized with sliding array.

        In the recursive formula, current state is just dependent on its neighbors on the
        right and below. So we are just making use of a auxiliary array of length n. So we
        can slide the array to reduce space complexity.
        """
        m, n = len(dungeon), len(dungeon[0])
        hp = [1 << 31] * (n + 1)
        # dummy variables to make it clean
        hp[n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                hp[j] = max(1, min(hp[j], hp[j + 1]) - dungeon[i][j])
                pass
        print(hp)
        return hp[0]

def test():
    solution = Solution()
    assert solution.calculateMinimumHP([[0]]) == 1
    assert solution.calculateMinimumHP([
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]]) == 7
    print('self test passed')

if __name__ == '__main__':
    test()
