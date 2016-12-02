#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
122. Best Time to Buy and Sell Stock II

Total Accepted: 114527
Total Submissions: 253971
Difficulty: Medium
Contributors: Admin

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as
you like (ie, buy one and sell one share of the stock multiple times). However, you may
not engage in multiple transactions at the same time (ie, you must sell the stock before
you buy again).

==============================================================================================
SOLUTION:
    Sum up the positive difference values in DIFFERENCE ARRAY.
'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfitShort(prices)

    def maxProfitBasic(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                result += prices[i] - prices[i - 1]
                pass
        return result

    def maxProfitShort(self, prices):
        return sum(j - i for (i, j) in zip(prices[:-1], prices[1:]) if j >= i)
