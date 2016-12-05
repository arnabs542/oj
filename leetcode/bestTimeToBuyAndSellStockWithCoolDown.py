#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
309. Best Time to Buy and Sell Stock with Cooldown

Total Accepted: 30446
Total Submissions: 77568
Difficulty: Medium
Contributors: Admin

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions
as you like (ie, buy one and sell one share of the stock multiple times) with the following
cooldownrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock
before you buy again).

After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

    prices = [1, 2, 3, 0, 2]
    maxProfit = 3
    transactions = [buy, sell, cooldown, buy, sell]

==============================================================================================
SOLUTION:

Overlapping subproblems with optimal substructures.

1. Define STATE:
    f(i): maximum profit we can get at day i.
Then we have two scenarios for each day: we sell here or not.

f(i) = max(f(i - 1), max(f(j - 2) + prices[i] - prices[j]))
     = max(f(i - 1), prices[i] + max(f(j - 2) - prices[j])), j = 0, 1, ..., i - 1
, where i is the day index, and j is the last day we buy the stock.

While scanning the prices list, we keep track of max(f(j - 2) - prices[j]) and update f(i).
Time compleixty is O(n), space complexity is O(n).

2. Another way of defining states and deduction with state machine

At each day, we have three possible actions: buy, sell, cooldown, leading to three states:
maximum profit ending with the most recent action of buy, sell, cooldown.

Then we keep track of those three states simultaneously, and update them with
recurrence relation:

    buy[i]      = max(buy[i - 1], cooldown[i - 1] - prices[i]),
    sell[i]     = max(sell[i - 1], buy[i - 1] + prices[i]),
    cooldown[i] = max(cooldown[i - 1], buy[i - 1], sell[i - 1]),

How to make sure we sell before we buy?
Because cooldown[i] >= buy[i], so we can rewrite 3rd equation to

    buy[i]      = max(buy[i - 1], cooldown[i - 1] - prices[i]),
    sell[i]     = max(sell[i - 1], buy[i - 1] + prices[i]),
    cooldown[i] = max(cooldown[i - 1], sell[i - 1])
From the new transition, such invalid transaction would never occur.

The transition can be reduced to:
    buy[i]  = max(buy[i - 1], sell[i - 2] - prices[i]),
    sell[i] = max(sell[i - 1], buy[i -1] + prices[i]),

Actually, above recurrence relation can be directly derived without considering
any cooldown[i] at all.


'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # return self.maxProfitDP(prices)
        # return self.maxProfitFSM(prices)
        return self.maxProfitFSMOpt(prices)

    def maxProfitDP(self, prices: list) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        # TODO: space complexity can be reduced, for sure
        f = [0] * (len(prices) + 1) # pad leading zero to neutralize empty list case
        diff = float('-inf') # f(j - 1) - prices[j]
        for i in range(1, len(prices) + 1):
            f[i] = max(f[i - 1], prices[i - 1] + diff)
            diff = max(diff, f[max(0, i - 2)] - prices[i - 1])
            pass
        print(f)
        return f[len(prices)]

    def maxProfitFSM(self, prices: list) -> int:
        '''
        Dynamic Programming in a finite state machine state fashion.
        '''
        m = len(prices) + 1
        buy, sell, cooldown = [float('-inf')] * m, [0] * m, [0] * m
        for i in range(1, len(prices) + 1):
            buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i - 1])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i - 1])
            cooldown[i] = max(cooldown[i - 1], buy[i - 1], sell[i - 1])
            pass
        return sell[len(prices)]

    def maxProfitFSMOpt(self, prices: list) -> int:
        '''
        Dynamic Programming in a finite state machine state fashion.

        Current state only depends on previous 2 states, only 2 variables
        are necessary.
        '''
        buy0, buy1, sell0, sell1 = float('-inf'), float('-inf'), 0, 0
        for i, price in enumerate(prices):
            buy0 = buy1
            buy1 = max(buy1, sell0 - prices[i])
            sell0 = sell1
            sell1 = max(sell1, buy0 + prices[i])
        return sell1

def test():
    solution = Solution()

    assert solution.maxProfit([]) == 0
    assert solution.maxProfit([2]) == 0
    assert solution.maxProfit([2, 1]) == 0
    assert solution.maxProfit([3, 9]) == 6
    assert solution.maxProfit([1, 3, 9]) == 8
    assert solution.maxProfit([1, 2, 3, 0, 2]) == 3

    print('self test passed')

if __name__ == '__main__':
    test()
