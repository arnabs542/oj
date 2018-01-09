#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Egg dropping puzzle

The following is a description of the instance of this famous puzzle involving n=2 eggs and a building with H=36 floors

Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing (using U.S. English terminology, in which the first floor is at ground level). We make a few assumptions:
    An egg that survives a fall can be used again.
    A broken egg must be discarded.
    The effect of a fall is the same for all eggs.
    If an egg breaks when dropped, then it would break if dropped from a higher window.
    If an egg survives a fall, then it would survive a shorter fall.
    It is not ruled out that the first-floor windows break eggs, nor is it ruled out that eggs can survive the 36th-floor windows.

================================================================================

1. Linear search

Keep dropping the egg from lowest floor to highest, until it breaks.

Complexity: O(N)

2. Minimax - minimize worst case loss

If only one egg is available and we wish to be sure of obtaining the right result, the experiment can be carried out in only one way. Drop the egg from the first-floor window; if it survives, drop it from the second-floor window. Continue upward until it breaks. In the worst case, this method may require 36 droppings. Suppose 2 eggs are available. What is the lowest number of egg-droppings that is guaranteed to work in all cases?

Binary search?
This is a strategy, but, there is a more optimal solution...

Maybe not straightforward to come up with, but, at least, we can write a program
to find the solution.

--------------------------------------------------------------------------------
The idea is to MINIMIZE THE WORST CASE LOSS, using minimax!

To derive a dynamic programming functional equation for this puzzle, let the STATE of the dynamic programming model be a pair s = (n, k), where

n = number of test eggs available, n = 0, 1, 2, 3, ..., N − 1.
k = number of (consecutive) floors yet to be tested, k = 0, 1, 2, ..., H − 1.

Now, let
W(n,k) = minimum number of trials required to identify the value of the critical floor under the worst-case scenario given that the process is in state s = (n,k).

Then STATE TRANSITION RECURRENCE RELATION can be shown that

W(n, k) = 1 + min{max(W(n − 1, x − 1), W(n, k − x)): x = 1, 2, ..., k }
with W(n, 0) = 0 for all n > 0 and W(1, k) = k for all k.

Complexity: O(nk²), O(nk)

"""

from _decorators import memoize, timeit


class Solution:

    @timeit
    def dropEggs(self, nEggs, nFloors):
        """
        nEggs: number of eggs
        nFloors): number of floors
        """
        # result = self._dropEggsMinimaxDfs(nEggs, nFloors)
        result = self._dropEggsMinimaxDp(nEggs, nFloors)

        print(nEggs, nFloors, ' => ', result)

        return result

    def _dropEggsMinimaxDfs(self, nEggs, nFloors):
        @memoize
        def dfs(m, n):
            if n <= 0: return 0
            if m == 0: return float('inf')
            if m == 1: return max(n, 0)

            minimalLoss = float('inf')
            bestAction = None
            for i in range(1, n + 1):
                # drop at jth floor, two situations: broken or not broken
                worstCaseLoss = 1 + max(dfs(m - 1, i - 1), dfs(m, n - i))
                if worstCaseLoss < minimalLoss:
                    bestAction = i
                minimalLoss = min(minimalLoss, worstCaseLoss)

            print('at', (m, n), ', choose: ', bestAction, ', loss: ', minimalLoss)

            return minimalLoss

        return dfs(nEggs, nFloors)

    def _dropEggsMinimaxDp(self, m, n):
        # TODO:  dynamic programming solution
        dp = [[j if i == 1 else (0 if not j else float('inf')) for j in range(n + 1)] for i in range(m + 1)]
        for i in range(2, m + 1):
            for j in range(1, n + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[m][n]

def test():
    solution = Solution()

    assert solution.dropEggs(0, 0) == 0
    assert solution.dropEggs(1, 0) == 0
    assert solution.dropEggs(1, 1) == 1
    assert solution.dropEggs(1, 10) == 10
    assert solution.dropEggs(1, 100) == 100
    assert solution.dropEggs(2, 1) == 1
    assert solution.dropEggs(2, 2) == 2
    assert solution.dropEggs(2, 100) == 14

    print("self test passed")

if __name__ == '__main__':
    test()
