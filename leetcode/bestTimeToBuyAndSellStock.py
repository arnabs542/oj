#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
121. Best Time to Buy and Sell Stock

Total Accepted: 148007
Total Submissions: 382261
Difficulty: Easy
Contributors: Admin

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one
share of the stock), design an algorithm to find the maximum profit.

Example 1:
    Input: [7, 1, 5, 3, 6, 4]
    Output: 5

    max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than
buying price)

Example 2:
    Input: [7, 6, 4, 3, 1]
    Output: 0

    In this case, no transaction is done, i.e. max profit = 0.

==============================================================================================
SOLUTION:
    Requiring to get the maximum DIFFERENCE between two number.

1. Construct the DIFFERENCE ARRAY by replacing each element by the difference between itself
and the previous element, except for the first element, which we simply ignore.
Then the problem is reduced to "Maximum Subarray".

Note: Computing the DIFFERENCE ARRAY, and a PREFIX SUM array—are the discrete equivalents
of DIFFERENTIATION and INTEGRATION in calculus, which operates on continuous domains.

2. The maximum DIFFERENCE must be obtained by subtracting a LOCAL MAXIMUM by a LOCAL MINIMUM.
How about finding these two pointers?

3. In a perspective of QUANTITY CHANGE, denoted by delta, then each ACTION would cause a
QUANTITY CHANGE to current profit, increase or decrease. We keep track of such state:
    state = (quantity change after buying, quantity change after selling),

which means the change of profit after buying and selling respectively, and the latter depends
on the former one. Then we have clear RECURRENCE RELATION to update the state while scanning
the prices array. Mind the update order of the state.
'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # return self.maxProfitDPSubarray(prices)
        # return self.maxProfitTwoPointers(prices)
        return self.maxProfitDP(prices)

    def maxProfitDPSubarray(self, prices: list) -> int:
        """
        :type prices: List[int]
        :rtype: int

        Difference array with maximum subarray solution
        """
        diff = map(lambda x: (x[1] - prices[x[0] - 1]) if x[0] else 0,
                   enumerate(prices))
        max_ending_here, max_so_far = 0, 0
        for _, d in enumerate(diff):
            max_ending_here = max(0, max_ending_here + d)
            max_so_far = max(max_so_far, max_ending_here)

        print(max_so_far)
        return max_so_far

    def maxProfitTwoPointers(self, prices: list) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: return 0
        minimum, max_so_far = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]: minimum = min(minimum, prices[i])
            else: max_so_far = max(max_so_far, prices[i] - minimum)
            pass
        print(max_so_far)
        return max_so_far

    def maxProfitDP(self, prices: list) -> int:
        """
        :type prices: List[int]
        :rtype: int

        STATE = (profit change by buying, profit change by selling)
        """
        # XXX: STATE definition is more subtle and generalizes well
        change_buy, change_sell = float('-inf'), 0
        for p in prices:
            change_sell = max(change_sell, change_buy + p)
            change_buy = max(change_buy, -p)
        return change_sell

def test():
    solution = Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0

    print('self test passed')

if __name__ == '__main__':
    test()
