'''
Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie,
buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
# We can solve this problem using dynamic programming,of which the time complexity
# is O(n)

class Solution:

    def maxSubarray(self, changes):
        begin = 0
        begin_temp = 0
        end = 0
        max_so_far = 0
        max_ending_here = 0
        for i in range(len(changes[0:])):
            if max_ending_here > 0:
                max_ending_here += changes[i]
            else:
                max_ending_here = changes[i]
                begin_temp = i

            if max_ending_here > max_so_far:
                begin = begin_temp
                end = i
                max_so_far = max_ending_here

        return begin, end, max_so_far

    # @param prices,a list of integer
    # @return an integer
    def maxProfit(self, prices):
        changes = []
        for i in range(len(prices) - 1):
            changes.append(prices[i + 1] - prices[i])

        begin, end, max_so_far = self.maxSubarray(changes)
        return max_so_far


if __name__ == "__main__":
    pass
