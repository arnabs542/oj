#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A balance puzzle or weighing puzzle is a logic puzzle about balancing items—often coins—to determine which holds a different value, by using balance scales a limited number of times. These differ from puzzles that assign weights to items, in that only the relative mass of these items is relevant.

Now, we are given 12 coins, one of them is heavier than others.

Reference:
https://www.av8n.com/physics/twelve-coins.htm


================================================================================
SOLUTION

The core idea is about SPLIT SEARCH STATE SPACE,
minimax (minimizing worst case loss), INFORMATION GAIN.

1. Brute force - linear search strategy

Take a coin, weigh every other coin with it to find the one that's heavier.

Complexity: O(N).

2. Binary search strategy
Of course, we can split the search space by two every time.

Complexity: O(log₂N)

Key observation - information gain
----------------------------------
The balance provides one of three possible indications:
the right pan is heavier, or the pans are in balance, or the left pan is heavier.

3. Minimax to find the optimal strategy

The core idea is to MINIMIZE WORST CASE LOSS.

Give n coins, use the balance scales to weigh some coins then split the search space.

The question is, how to split the coins to weigh?
Well, if we don't know the strategy yet, we can at least do exhaustive search,
with minimax algorithm.

The idea is to harness recurrence relation.
Select a number of coins to evenly put x coins in two arms of the balance scales.
Use the balance scales to weigh once, then the information we can get will
give conclusions.
1) unbalanced: the target coin is on the side of the balance that's heavier, 1/x.
2) balanced: the target coin in among the rest of coins not on the balance, 1/(n-2x).

Minimax recurrence relation
-------------------
f(x) = min(f(x), 1 + max(f(i), f(x - 2 * i))), i = 1, 2, ..., x // 2

Complexity
----------
The state space is one dimensional, within range [1, N]. Then without duplicate
computations, the time complexity is O(N).

4. Logarithm search with base 3

Split the search space into 3 disjoint sets.

Complexity
----------
The state space is one dimensional number, with range [1, logN]. When duplicate
computations are eliminated, with memoization, the time complexity is O(log₃N).

4. Closed form formula
A more abstraction from the above minimax optimization algorithm leads to
variant of binary search: three way search!

Divide the coins into 3 groups as evenly as possible, then there are at most
two groups of same size(pigeonhole principle).
Weigh two groups of same size, and make use of the same recurrence relation above.

Complexity: O(1)

################################################################################
FOLLOW UP
1. Use the balance at most 3 times, what is the maximum number of coins that
we can find the heavier one from?

Use recurrence relation to derive, or even a more abstract mathematical
closed form equation: log₃N, where N is the number of total coins.

2. What if we don't know whether the target coin is heavier or lighter?

"""

from functools import lru_cache
import math

from _decorators import memoize

class Solution:

    def findHeavierCoin(self, n):
        # result = self._findHeavierCoinMinimax(n)
        result = self._findHeavierCoinThreeWaySearch(n)
        # result = self._findHeavierCoinClosedForm(n)

        print(n, result)

        return result

    def _findHeavierCoinMinimax(self, n):
        @lru_cache(maxsize=None)
        # @memoize
        def dfs(x):
            # base cases
            if x <= 1: return 0
            if x in (2, 3): return 1

            nSteps = float('inf')
            # recurrence relation: weigh once and split
            for i in range(1, x // 2 + 1):
                # minimax: minimize worst case loss
                nSteps = min(nSteps, 1 + max(dfs(i), dfs(x - 2 * i)))
            # print(x, nSteps)
            return nSteps

        return dfs(n)

    def _findHeavierCoinThreeWaySearch(self, n):
        """
        Variant to binary search: three way search to split the search space into
        three disjoint sets.
        """
        def dfs(x):
            if x <= 1: return 0
            if x in (2, 3): return 1

            d, r = divmod(x, 3)
            return dfs(d + r) + 1

        return dfs(n)

    def _findHeavierCoinClosedForm(self, n):
        return math.ceil(math.log(n, 3))

    def _findDifferntCoinMinimax(self, n):
        """
        Find the coin with different weight, can be either heavier or lighter.
        """
        @lru_cache(maxsize=None)
        def dfs(x):
            # base cases
            if x <= 1: return 0
            if x == 2: return float('inf')
            if x in (3,): return 2
            if x == 4: return 2

            nSteps = float('inf')
            # recurrence relation: weigh once and split
            for i in range(1, (x  + 1)// 2):
                # minimax: minimize worst case loss
                # nSteps = min(nSteps, 1 + max(dfs(2 * i), min(dfs(x - 2 * i), dfs(x - 2 * i))))
                nSteps = min(nSteps, 1 + max(dfs(x - 2 * i), dfs(i)))
            print(x, nSteps)
            return nSteps

        return dfs(n)

def test():
    solution = Solution()

    print("test: target coin is heavier")

    # target coin is heavier
    assert solution.findHeavierCoin(1) == 0
    assert solution.findHeavierCoin(2) == 1
    assert solution.findHeavierCoin(3) == 1 # log₃3 = 1
    assert solution.findHeavierCoin(4) == 2 # log₃3 = 1
    assert solution.findHeavierCoin(9) == 2 # log₃9 = 2
    assert solution.findHeavierCoin(12) == 3
    assert solution.findHeavierCoin(16) == 3
    assert solution.findHeavierCoin(27) == 3 # log₃27 = 3
    assert solution.findHeavierCoin(28) == 4 # log₃27 = 3
    assert solution.findHeavierCoin(81) == 4 # log₃81 = 4
    assert solution.findHeavierCoin(100) == 5 # log₃100 <= 5
    assert solution.findHeavierCoin(1000) == 7 # log₃100 = 6.28

    print("test: target coin is weight unkown")

    # target coin's weight is known: can be heavier or lighter
    # assert solution._findDifferentCoinMinimax(1) == 0
    # assert solution._findDifferentCoinMinimax(2) == float('inf')
    # assert solution._findDifferentCoinMinimax(3) == 2
    # assert solution._findDifferentCoinMinimax(4) == 2
    # assert solution._findDifferentCoinMinimax(12) == 3

    print("self test passed!")

if __name__ == '__main__':
    test()
