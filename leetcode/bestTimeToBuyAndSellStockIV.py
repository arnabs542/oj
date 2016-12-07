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
SOLUTION:
    Dynamic Programming.

1. TWO DIMENSIONAL STATE.

f[k, j] represents the max profit up till prices[j] using at most k transactions.

∵ At each point, there are two scenarios:
    1) sell at here: merge the last transaction
    2) not to sell here: use the previous state's result
∴
f[k, j] = max(f[k, j-1], prices[j] - prices[jj] + f[k-1, jj]), where jj = 0, ..., j - 1
        = max(f[k, j-1], prices[j] + max(f[k-1, jj] - prices[jj]))

f[0, j] = 0; 0 transactions makes 0 profit
f[k, 0] = 0; if there is only one price data point you can't make any transaction.

Time complexity: O(nk), space complexity: O(nk).

But we can reduce the space complexity in a quantity change perspective.

2. Linear dynamic programming in QUANTITY CHANGE/ STATE MACHINE perspective.

Without limit on k, to obtain the maximum profit, we just sum up the difference along all
ascending subsequences/subarrays. And when k decreases, there might be some subsequence
merging into one larger than any of those two to save number of transactions. And the
difference of merged subarray is smaller than the sum of two individual differences.
Strategies:
    1. Buy at local minimum(valley) and sell at local maximum(peak) in an ASCENDING
subsequence.

In a perspective of DERIVATIVES in calculus:

    The function's difference between two points, is the AREA under curve of its first-order
derivative function between two points. Positive derivatives give positive area, and vice
versa. And positive derivatives indicates increasing function. Derivatives indicate quantity
change rate. In discrete domain, derivatives can be viewed as difference(quantity change).

    The total profit can be defined as a function f(X), where X is a sequence of actions,
each of which is one of buy and sell. And we want to find the max(f). Then we follow a
path with positive derivatives(differences) to get the maximum value.

----------------------------------------------------------------------------------------------
In a perspective of STATE MACHINE:

At each day, we have two possible ACTIONS giving two scenarios with STATES:
    maximum profit ending with last action of buy
    maximum profit ending with last action of sell

Define the STATE as a 2k-tuple profit quantity change:
    (
        quantity change after first release, # to buy is to hold
        quantity change after first hold, # to sell is to release
        quantity change after 2nd release,
        quantity change after 2nd hold,
        ...,
        quantity change after kth release,
        quantity change after kth hold,
    )

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
        if k > len(prices) // 2: return self.maxProfitNoLimit(prices)
        # return self.maxProfitDP2D(k, prices)
        return self.maxProfitDPQuantityChange(k, prices)
        # return self.maxProfitDPQuantityChange2(k, prices)

    def maxProfitNoLimit(self, prices: list) -> int:
        # return sum(map(
            # lambda x: max(0, x[1] - prices[x[0] - 1]) if x[0] else 0,
            # enumerate(prices)))
            return sum(j - i for (i, j) in zip(prices[:-1], prices[1:]) if j >= i)

    def maxProfitDP2D(self, k, prices: list) -> int:
        '''
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

    def maxProfitDPQuantityChange(self, k, prices: list) -> int:
        '''
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
        # TODO: better illustration of why this algorithm would work
        # call the procedure without number of transactions limit instead
        # 2 trailing padding zeroes to neutralize the k == 0 corner case
        state = [0 if i % 2 else float('-inf') for i in range(2 * (k + 1))]
        for p in prices:
            for i in range(2 * k - 1, -1, -1):
                # XXX: reverse/decreasing order to ensure number in prices is used only
                # once to make sure we sell before buy
                state[i] = max(state[i], (i and state[i - 1]) + p * -pow(-1, i % 2))

        print(state)
        return state[2 * k - 1]

    def maxProfitDPQuantityChange2(self, k, prices: list) -> int:
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
