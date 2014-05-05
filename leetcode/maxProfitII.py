'''
Best Time to Buy and Sell Stock II

Say you have an array for which the ith element is the
price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete
as many transactions as you like (ie, buy one and sell one share of
the stock multiple times). However, you may not engage in multiple transactions
at the same time (ie, you must sell the stock before you buy again).
'''

class Solution:
    # @param prices,a list of integer
    # @return an integer
    def maxProfit(self,prices):
        changes = []
        for i in range(len(prices)-1):
            changes.append(prices[i+1]-prices[i])

        max_sum = 0
        for x in changes:
            if x > 0:
                max_sum += x

        return max_sum

if __name__ == "__main__":
    pass
