#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
123. Best Time to Buy and Sell Stock III

Total Accepted: 72924
Total Submissions: 260292
Difficulty: Hard
Contributors: Admin

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock
before you buy again).

==============================================================================================
SOLUTION:
    In a perspective of DERIVATIVES: Without limit of number of transactions, we could compute
the AREA under it first-order derivative function curve (sum up the difference) where first
order derivative is positive (along all ascending subsequences/subarrays).

Optimal Substructure OBSERVATION:
    the two non-overlapping transactions must both be some maximum subarray(in difference
array) within their non-overlapping subarray range, which can be shown by
PROOF BY CONTRADICTION:  Because we can always get better optimized solution by replacing one
of them with a larger subarray, otherwise.

1. Brute-force.
For array with length l, we define the STATE as a 3-tuple:
    (maximum subarray, maximum profit, maximum subarray ending here)
Then, in a bottom-up approach, element at current position have two scenarios:
    1) sell stock here: split the array into two, take the first part's maximum subaray, and
and second part's maximum subarray ending with current position.
    2) Not to sell stock here: reduced to case where length is l - 1

Maximum subarray: O(N * 1) = O(N).
Deciding where to split: worst O(N * N) = O(N²).
Overall time Complexity: worst O(N²).

2. Divide and Conquer
Based on the optimal substructure observation, we can divide and conquer: split the array
into two, take the maximum subarray from left and right, and keep track of the maximum sum.

3. Two dimensional Dynamic Programing.
State = f[k, j], indicating maximum profit with at most k transactions till prices[j].

4. One Dimensional Dynamic Programming, in a QUANTITY CHANGE perspective.
See 'bestTimeToBuyAndSellStock.py' method 3. Define the STATE as a 4-tuple quantity change:
    (
        quantity change after first buying,
        quantity change after first selling,
        quantity change after second buying,
        quantity change after second selling,
    )
Because we have to sell before buying again, so we need to update the 4-tuple in reverse order
while scanning the array.

'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # return self.maxProfitDPNaive(prices)
        # return self.maxProfitDivideAndConquer(prices)
        return self.maxProfitDPQuantityChange(prices)

    def maxProfitDPNaive(self, prices: list) -> int:
        '''
        STATE = (max subarray, max profit, max_ending_here)

        time complexity: O(N²)
        '''
        diff = list(map(lambda x: x[1] - prices[x[0] - 1] if x[0] else 0,
                        enumerate(prices)))
        f = [[0] * 2 for _ in range(len(prices) + 1)] # max subarray, max profit
        max_ending_here = 0
        for i in range(1, len(prices) + 1):
            max_ending_here = max(max_ending_here + diff[i - 1], 0)
            f[i][0] = max(f[i - 1][0], max_ending_here)
            f[i][1] = f[i - 1][1] # don't sell at this time
            # FIXME(fixed): tackle time limit exceeded by filtering
            if diff[i - 1] <= 0: continue
            for j in range(1, i): # sell at this time
                f[i][1] = max(f[i][1], prices[i - 1] - prices[j - 1] + f[j - 1][0])
        return f[-1][1]

    def maxProfitDivideAndConquer(self, prices: list) -> int:
        '''
        Optimized dynamic programming solution:
            Split the array into two, divide and conquer with PREPROCESSING MEMOIZATION.

        Compute all the maximum subarray in [0, i] and [i, N - 1], where i is in [0, N - 1].
        Then, do a linear scan to get sum of two subsets' maximum subarray.
        It take two passes to compute the maximum subarray, O(2N), and one pass to get the
        maximum sum, O(N). Overall time complexity is O(N).

        Time complexity: O(N)
        '''
        if len(prices) < 2: return 0
        left = [0] * len(prices)
        low = prices[0]
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            left[i] = max(left[i - 1], prices[i] - low)
        right = [0] * (len(prices) + 1)
        high = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            high = max(high, prices[i])
            right[i] = max(right[i + 1], high - prices[i])

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, left[i] + right[i])
        return max_profit

    def maxProfitDPQuantityChange(self, prices: list) -> int:
        '''
        STATE =  (
            quantity change after first buying,
            quantity change after first selling,
            quantity change after second buying,
            quantity change after second selling,
        )
        '''
        state = [float('-inf'), 0, float('-inf'), 0]
        for p in prices:
            state[3] = max(state[3], state[2] + p)
            state[2] = max(state[2], state[1] - p)
            state[1] = max(state[1], state[0] + p)
            state[0] = max(state[0], -p)
        print(state)
        return state[-1]

def test():
    solution = Solution()

    assert solution.maxProfit([]) == 0
    assert solution.maxProfit([1, 2, 3, 4, 5, 6, 7]) == 6
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    assert solution.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6

    print('self test passed')

if __name__ == '__main__':
    test()
