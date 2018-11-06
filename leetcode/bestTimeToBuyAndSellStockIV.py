#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
188. Best Time to Buy and Sell Stock IV

Total Accepted: 37299
Total Submissions: 157749
Difficulty: Hard
Contributors: Admin

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock
before you buy again).

==============================================================================================
SOLUTION

This is a generalized problem of "Best Time to Buy and Sell Stock III".
Try to exploit the state transition with dynamic programming.

The generalized solution is exploited in last section of "Best Time To Buy and Sell Stock III".

1. Dynamic programming with two dimensional state.

Define state
------------
f[n, k] represents the max profit up till prices[n] with at most k transactions.

Recurrence relation
-------------------
∵ At each point, there are two scenarios:
    1) sell at here: merge the last transaction
    2) not to sell here: use the previous state's result
∴
f[n, k] = max(f[n-1, k], prices[n] - prices[j] + f[j, k-1]), where j = 0, ..., n - 1
        = max(f[n-1, k], prices[n] + max(f[j, k-1] - prices[jj]))

f[n, 0] = 0; 0 transactions makes 0 profit
f[0, k] = 0; if there is only one price data point you can't make any transaction.

In this recurrence relation, the algorithm needs to iterate through an inner loop,
with index j in range [0, n], to decide the optimal choice of when to buy. And
this loop is O(n).

Time complexity: O(n²k), space complexity: O(nk).

But we can reduce the space complexity in a quantity change perspective.

2. Linear dynamic programming with another dimension of state.

Time space trade off
--------------------
The core idea is to TRADE SPACE FOR TIME.

Previous bottleneck
-------------------
In the above state transition, the algorithm needs to iterate through an inner loop,
with index j in range [0, n], to decide the optimal choice of when to buy. And
this loop is O(n).

How about use another dimension of state to keep track of that information?

--------------------------------------------------------------------------------
This is an optimization to reduce the inner loop for deciding where to buy,
with the trick of TRADE SPACE FOR TIME, a.w.a add another dimension of state.
--------------------------------------------------------------------------------

Refer to "./bestTimeToBuyAndSellStockIII.py".

Define state
------------
Define 3D state f(n, k, p) as the profit gain within [0, n],
with kₜₕ transition, to buy if p == 0 or sell, in a QUANTITY CHANGE perspective,

At each day, we have 3 possible ACTIONS giving two scenarios:
    maximum profit ending with last action of buy
    maximum profit ending with last action of sell
    do nothing(just wait)

State transition recurrence relation
------------------------------------
    f(n, k, 0) = max(f(n, k, 0), f(n - 1, k - 1, 1) - prices[n]) # buy here
    f(n, k, 1) = max(f(n, k, 1), f(n - 1, k - 1, 0) + prices[n]) # sell here
    # do nothing here is tracked by f(n, k - 1, 1).

Note on space optimization
--------------------------
The above state can be flattened into 2k-tuple profit quantity change:
    (
        quantity change after first release, # to buy is to hold
        quantity change after first hold, # to sell is to release
        quantity change after 2nd release,
        quantity change after 2nd hold,
        ...,
        quantity change after kth release,
        quantity change after kth hold,
    )

Recurrence relation
-------------------
Recurrence relation/state transition through action:

    release[i] = max(release[i], hold[i] + prices[j])
    hold[i]    = max(hold[i], release[i - 1] - prices[j])
    ...
    release[0] = max(release[0], hold[0] + prices[j])
    hold[0]    = max(hold[0], -prices[j])

Time complexity: O(nk), reduced space complexity: O(k).

Update the 2k-tuple in reverse order while scanning the array, because we have to sell before
buy again.

NOTE:
    When k > len(prices) // 2, the problem is reduced to max profit without limit on number of
transactions.


'''

class Solution(object):

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # FIXED: memory error and time limit exceeded when k > len(prices) // 2
        if k > len(prices) // 2: result = self._maxProfitNoLimit(prices)
        else:
            # result = self._maxProfitDP2D(k, prices)
            result = self._maxProfitDPQuantityChange(k, prices)
            # result = self._maxProfitDPQuantityChange2(k, prices)

        print(prices, k, " result: ", result)

        return result

    def _maxProfitNoLimit(self, prices: list) -> int:
        # return sum(map(
            # lambda x: max(0, x[1] - prices[x[0] - 1]) if x[0] else 0,
            # enumerate(prices)))
            return sum(j - i for (i, j) in zip(prices[:-1], prices[1:]) if j >= i)

    def _maxProfitDP2D(self, k, prices: list) -> int:
        '''
        Dynamic programming state transition in recurrence relation

        Define state two dimensional f(k, j)
        ------------------------------------
        f[k, j] represents the max profit up till prices[j] using at most k transactions.
        f[k, j] = max(f[k, j-1], prices[j] - prices[jj] + f[k-1, jj]), jj = 0, ..., j-1
                 = max(f[k, j-1], prices[j] + max(f[k-1, jj] - prices[jj]))
        f[0, j] = 0; 0 transactions makes 0 profit
        f[k, 0] = 0; if there is only one price data point you can't make any transaction.
        '''
        # DONE: two dimensional dynamic programming
        f = [[0] * (len(prices) + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            localMax = float('-inf')
            for j in range(1, len(prices) + 1):
                localMax = max(localMax, f[i - 1][j] - prices[j - 1])
                f[i][j] = max(f[i][j - 1], prices[j - 1] + localMax)
                pass
        print(f[:])
        return f[k][len(prices)]

    def _maxProfitDPQuantityChange(self, k, prices: list) -> int:
        '''
        Space optimized:
            State transition table reduced from 2-dimension to 1-dimension,
        since the recurrence relation only last 1 column.

        STATE = (
                quantity change after first buying,
                quantity change after first selling,
                quantity change after 2nd buying,
                quantity change after 2nd selling,
                ...,
                quantity change after kth selling,
                quantity change after kth selling,
                )
        '''
        # call the procedure without number of transactions limit instead
        # 2 trailing padding zeroes to neutralize the k == 0 corner case
        state = [0 if i % 2 else float('-inf') for i in range(2 * (k + 1))]
        for p in prices:
            for i in range(2 * k - 1, -1, -1):
                # XXX: reverse/decreasing topological order of dependency graph
                # to ensure number in prices is used only once to make sure we sell before buy
                state[i] = max(state[i], (i and state[i - 1]) + p * -pow(-1, i % 2))

        print(state)
        return state[2 * k - 1]

    def _maxProfitDPQuantityChange2(self, k, prices: list) -> int:
        '''
        More readable version of maxProfitDPQuantityChange
        '''
        hold = [float('-inf')] * (k + 1) # pad leading zero to neutralize empty list case
        release = [0] * (k + 1)
        for p in prices:
            for i in range(k, 0, -1):
                release[i] = max(release[i], hold[i] + p)
                hold[i] = max(hold[i], release[i - 1] - p)

        return release[k]

def test():
    solution = Solution()

    print("corner cases")
    assert solution.maxProfit(2, []) == 0
    assert solution.maxProfit(0, [1, 3]) == 0

    print("\nincreasing sequence")
    assert solution.maxProfit(2, [1, 2, 3, 4]) == 3
    print("\ndecreasing sequence")
    assert solution.maxProfit(2, [7, 6, 4, 3, 1]) == 0

    print('\ndifferent k')
    assert solution.maxProfit(1, [7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit(2, [7, 1, 5, 3, 6, 4]) == 7
    assert solution.maxProfit(3, [7, 1, 5, 3, 6, 4]) == 7

    assert solution.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert solution.maxProfit(3, [3, 3, 5, 0, 0, 3, 1, 4]) == 8

    print('\nsequence derivatives changes', 2)
    assert solution.maxProfit(2, [1, 4, 5, 7]) == 6
    assert solution.maxProfit(2, [1, 5, 4, 7]) == 7
    assert solution.maxProfit(2, [1, 5, 4, 7, 2]) == 7
    assert solution.maxProfit(2, [1, 5, 4, 7, 2, 3]) == 7
    assert solution.maxProfit(2, [1, 5, 4, 7, 2, 9]) == 13

    print('\nsequence derivatives changes', 3)
    assert solution.maxProfit(3, [1, 5, 4, 7, 3, 2, 1, 0]) == 7
    assert solution.maxProfit(3, [1, 5, 4, 7, 2, 3]) == 8
    assert solution.maxProfit(3, [1, 5, 4, 7, 2, 9]) == 14
    print('\nself test passed')

if __name__ == '__main__':
    test()
