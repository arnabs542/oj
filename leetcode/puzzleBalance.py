#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A balance puzzle or weighing puzzle is a logic puzzle about balancing items—often coins—to determine which holds a different value, by using balance scales a limited number of times. These differ from puzzles that assign weights to items, in that only the relative mass of these items is relevant.

Now, we are given 12 coins, one of them is heavier than others.

Reference:
https://en.wikipedia.org/wiki/Balance_puzzle
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

3. Minimax strategy - MINIMIZE WORST CASE LOSS with recurrence relation

Reduce the problem into a simpler form and exploit the recurrence relation!

To reduce it, we have to measure two groups of coins of same size first.
Then based on the result of the balance scales, we have different decisions to make.

The question is, how to split the coins to weigh for the first time?
Do EXHAUSTIVE SEARCH, with minimax algorithm!

Key observation - information gain
----------------------------------
The balance provides one of three possible indications:
the right pan is heavier, or the pans are in balance, or the left pan is heavier.

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

4. Logarithm search with base 3 - trichotomy

The strategy is to divide the coins as evenly as possible into 3 sets.

And n = 3 * m + r, where m is the quotient and r is remainder and r = 0, 1, 2.

Then it can be divided into m, m, m + r.
If r % 2 == 0, then we can also divide it into m + r/2, m + r/2, m.
If r % 2 == 1, then divide into m, m, m + r=m+1.

Split the search space into 3 disjoint sets, since weighing once with the balance
will give information to classify 3 different sets of coins:
left arm coins, right arm coins, unweighed coins.

Complexity
----------
The state space is one dimensional number, with range [1, log₃N]. When duplicate
computations are eliminated, with memoization, the time complexity is O(log₃N).

4. Closed form formula
A more abstraction from the above minimax optimization algorithm leads to
variant of binary search: three way search!

Divide the coins into 3 groups as EVENLY as possible(balanced split), then there are at least
two groups of same size(pigeonhole principle).
Weigh two groups of same size, and make use of the same recurrence relation above.

Complexity: O(1)

################################################################################
FOLLOW UP
1. Use the balance at most 3 times, what is the maximum number of coins that
we can find the heavier one from?

Use recurrence relation to derive, or even a more abstract mathematical
closed form equation: 3ⁿ, where n is the number of total coins.

2. What if we don't know whether the target coin is heavier or lighter?
In this scenario, weighing once with the balance, with i coins on both side
will give information:
1) left pan is heavier: different coin is on the balance, 1 / 2i
2) right pan is heavier: same as above, 1 / 2i
3) balanced: different coin is not on the balance, 1 / (n - 2i)

Strategy:
Split the coins into 2 equal size groups, and distribute one group evenly on
two sides of the balance.

"""

from functools import lru_cache
import math

from _decorators import memoize

class Solution:

    def findCoinHeavier(self, n):
        # result = self._findCoinHeavierMinimax(n)
        # result = self._findCoinHeavierThreeWaySearch(n)
        result = self._findCoinHeavierClosedForm(n)

        print(n, result)

        return result

    def _findCoinHeavierMinimax(self, n):
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

    def _findCoinHeavierThreeWaySearch(self, n):
        """
        Variant to binary search: three way search to split the search space into
        three disjoint sets, a.k.a, trichotomy.
        """
        def dfs(x):
            if x <= 1: return 0
            if x in (2, 3): return 1

            d, r = divmod(x, 3)
            return dfs(d + r) + 1

        return dfs(n)

    def _findCoinHeavierClosedForm(self, n):
        return math.ceil(math.log(n, 3))

    def _findCoinDifferentThreeWaySearch(self, n):
        pass

    def _findCoinDifferentMinimax(self, n):
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

            loss = float('inf')
            j = None # reduced to problem of size j
            # recurrence relation: weigh once and split
            for i in range(1, (x  + 1)// 2):
                # minimax: minimize worst case loss
                # loss = min(loss, 1 + max(dfs(2 * i), min(dfs(x - 2 * i), dfs(x - 2 * i))))
                # worstCaseLoss = 1 + max(dfs(x - 2 * i), dfs(i))
                worstCaseLoss = 1 + max(dfs(max(x - 2 * i, 3)), min(dfs(max(2 * i, 3)),1 + dfs(i) if x - 2*i >= i else float('inf')))
                # if i <= x - 2 * i:
                    # worstCaseLoss = min(worstCaseLoss, 2 + dfs(i))
                # loss = min(loss, worstCaseLoss)
                if worstCaseLoss < loss:
                    loss = worstCaseLoss
                    j = i
            print('different coin: ', x, 'loss: ', loss, 'first weigh: ', j)
            return loss

        return dfs(n)

def test():
    solution = Solution()

    print("test: target coin is heavier")

    # target coin is heavier
    assert solution.findCoinHeavier(1) == 0
    assert solution.findCoinHeavier(2) == 1
    assert solution.findCoinHeavier(3) == 1 # log₃3 = 1
    assert solution.findCoinHeavier(4) == 2 # log₃3 = 1
    assert solution.findCoinHeavier(9) == 2 # log₃9 = 2
    assert solution.findCoinHeavier(12) == 3
    assert solution.findCoinHeavier(16) == 3
    assert solution.findCoinHeavier(27) == 3 # log₃27 = 3
    assert solution.findCoinHeavier(28) == 4 # log₃27 = 3
    assert solution.findCoinHeavier(81) == 4 # log₃81 = 4
    assert solution.findCoinHeavier(100) == 5 # log₃100 <= 5
    assert solution.findCoinHeavier(1000) == 7 # log₃100 = 6.28

    print("\ntest: target coin is weight unkown")

    # target coin's weight is known: can be heavier or lighter
    assert solution._findCoinDifferentMinimax(1) == 0
    assert solution._findCoinDifferentMinimax(2) == float('inf')
    assert solution._findCoinDifferentMinimax(3) == 2
    assert solution._findCoinDifferentMinimax(4) == 2
    assert solution._findCoinDifferentMinimax(5) == 3
    assert solution._findCoinDifferentMinimax(6) == 3
    assert solution._findCoinDifferentMinimax(12) == 3
    assert solution._findCoinDifferentMinimax(13) == 4

    print("self test passed!")

if __name__ == '__main__':
    test()
