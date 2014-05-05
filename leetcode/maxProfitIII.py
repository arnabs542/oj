'''
Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    '''

class Solution:
    def maxSubarray(self,changes):
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

        return begin,end,max_so_far



    # @param prices: a list of integers
    # @return an integer
    def maxProfit(self,prices):
        changes = []
        for i in range(len(prices)-1):
            changes.append(prices[i+1]-prices[i])

        begin_first,end_first,max_first = self.maxSubarray(changes)
        a,b,c = self.maxSubarray(changes[0:begin_first])
        a1,b1,c1 = self.maxSubarray(changes[end_first + 1:len(changes)])
        max_second = max(c,c1)

        return max_first + max_second


if __name__ == "__main__":
    print Solution().maxProfit([1,2,4])



