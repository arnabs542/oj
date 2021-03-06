#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
486. Predict the Winner

Total Accepted: 9314
Total Submissions: 21001
Difficulty: Medium
Contributors:
sameer13

Given an array of scores that are non-negative integers. Player 1 picks one of the
numbers from either end of the array followed by the player 2 and then player 1 and
so on. Each time a player picks a number, that number will not be available for the
next player. This continues until all the scores have been chosen. The player with
the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each
player plays to maximize his score.

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2
chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.

Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7.
No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True
representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.


================================================================================
SOLUTION

This is a multiple agent zero-sum game, and MINIMAX algorithm applies.
The ultimate state is whether a player wins or loses. But this state doesn't provide
full information for state transition.

The state transition recurrence relation depends on the exact sum of chosen numbers.
Define payoff function, as f = difference between scores of first and second player.
Then 1st player wins if f >= 0.

So, define state as a tuple:
    (
    score difference: difference of score to another player,
    (low, high): with available numbers in range [i, j]
    )

----------------------------------------------------------------------------------------------
In this multiplayer game, there are two players: maximizer and minimizer. In two alternative
steps, agents take their best actions to maximize/minimize the payoff function.

Since maximizing and minimizing are different logic, it would not be easy to directly use the
ultimate payoff function as state. With fundamental algebra knowledge, minimizing a function
is equivalent to maximizing its negative function. Then we can define an such player invariant
state that its negative value corresponds to its opponent's payoff function.

Then, we can define intermediate payoff function:
    f(a, low, high) = maximum difference between scores the first and second player can obtain with
given an array a from in [low, high].

Then the state transition for payoff function can be easily derived with MINIMAX:
    f[low][high] = max(nums[low] - f[low + 1][high], nums[high] - f[low][high - 1])

1. Recursive minimax - with memoization

And the subproblems are represented with states of interval. Apparently, they are overlapping.
So recursive implementation will be exponentially time consuming due to lots of redundant
calculation.

To adopt ITERATIVE approach, we must define state transition wisely.

Complexity
O(2???) without memoization
O(n??) with memoization


2. Dynamic programming with 2D state transition matrix
Complexity: O(N??), O(N??).

3. Space optimization
By drawing the state transition curve in the transition matrix, we can observe that current
state only depends on (i, j-1), (i+1, j). Then we can reduce the 2D transition matrix to a 1D
state transition column/row vector. If using a row vector, Then we fill the vector from
bottom to up, left to right.

-----------------------
...
    (i, j-1) ??? (i, j)

                ???

              (i+1, j)
...
-----------------------

'''

from _decorators import memoize

class Solution(object):

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = self._PredictTheWinnerMinimaxDfs(nums)
        # result = self._PredictTheWinnerMinimaxDp(nums)
        # result = self._PredictTheWinnerMinimaxSpaceOptimized(nums)

        print(nums, result)

        return result

    def _PredictTheWinnerMinimaxDfs(self, nums):
        @memoize
        def dfs(low, high):
            if not 0 <= low <= high <= len(nums) - 1: return 0
            diff = max(nums[low] - dfs(low + 1, high), nums[high] - dfs(low, high - 1))
            return diff
        return dfs(0, len(nums) - 1) >= 0

    def _PredictTheWinnerMinimaxDp(self, nums):
        f = [[0 for j in range(len(nums) + 2)] for i in range(len(nums) + 2)]
        for l in range(1, len(nums) + 1):
            for i in range(1, len(nums) + 2 - l):
                j = i + l - 1
                if l == 1:
                    f[i][j] = nums[i - 1]
                else:
                    f[i][j] = max(nums[i - 1] - f[i + 1][j], nums[j - 1] - f[i][j - 1])
        # print(f[1][len(nums)], f)
        return f[1][len(nums)] >= 0

    def _PredictTheWinnerMinimaxSpaceOptimized(self, nums):
        '''
        Linear space complexity for above minimax solution
        '''
        # DONE: improve in aspect of space complexity.
        f = [0 for j in range(len(nums) + 1)]
        for i in range(len(nums), 0, -1):
            for j in range(i, len(nums) + 1):
                if i == j: f[j] = nums[i - 1]
                else: f[j] = max(nums[i - 1] - f[j], nums[j - 1] - f[j - 1])
        return f[len(nums)] >= 0

def test():
    solution = Solution()

    a = []
    # assert solution.PredictTheWinner(a)

    a = [1]
    assert solution.PredictTheWinner(a)

    a = [1, 5]
    assert solution.PredictTheWinner(a)

    a = [1, 5, 2]
    assert not solution.PredictTheWinner(a)

    a = [1, 5, 233, 7]
    assert solution.PredictTheWinner(a)

    # import numpy as np
    # a = [np.random.randint(1, 1_000) for _ in range(20)]
    a = [549, 372, 753, 79, 249, 979, 520, 539, 270, 760, 210, 935, 274, 526, 33, 903, 914, 938, 52, 7]
    assert solution.PredictTheWinner(a)

    print("self test passed")

if __name__ == '__main__':
    test()
