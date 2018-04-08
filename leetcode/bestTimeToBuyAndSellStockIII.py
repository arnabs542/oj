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

================================================================================
SOLUTION

In a perspective of DERIVATIVES:
    Without limit of number of transactions, we could compute the AREA under its
first-order derivative function curve (sum up the difference), where first
order derivative is positive (along all ascending subsequences/subarrays).

Optimal Substructure OBSERVATION:
    the two non-overlapping transactions must both be some maximum subarray(in difference
array) within their non-overlapping subarray range, which can be shown by

PROOF BY CONTRADICTION:  Because we can always get better optimized solution by
replacing one of them with a larger subarray, otherwise.

1. Brute-force.

Exhaust all two subarrays that are not overlapping with each other.
Then linearly search for optimal sum of two subarrays.

Complexity
There are n(n-1)/2 subarrays, choosing two of them will yield complexity of O(n⁴).



I wrote these? I don't understand anymore...
For array with length l, we define the STATE as a 3-tuple:
    (maximum subarray, maximum profit, maximum subarray ending here)
Then, in a bottom-up approach, element at current position have two scenarios:
    1) sell stock here: split the array into two, take the first part's maximum subaray, and
and second part's maximum subarray ending with current position.
    2) Not to sell stock here: reduced to case where length is l - 1

Maximum subarray: O(N * 1) = O(N).
Deciding where to split: worst O(N * N) = O(N²).
Overall time Complexity: worst O(N²).


--------------------------------------------------------------------------------
Optimization with state transition

2. Divide and Conquer and sliding window

Exhausting subarrays will involve duplicate computations, since maximum subarray
can be solved in linear time.

Then we may resort to the process, in which we incrementally scan the list.

At each position i, find the maximum subarray so far within range [0, i],
and find the maximum subarray on the other end in [i + 1, n - 1].

Then we need to pre-compute maximum subarray with in range [0, i], [i + 1, n - 1],
for i = 0, ..., n - 1, both forward and backward.
Compute the maximum subarray within a range [i, j]. Then the state space is O(n²).
Fortunately this can be done in linear time with dynamic programming.

Complexity: O(n)


3. Two dimensional state dynamic programing

Define state as a tuple, function f(n, k) represents maximum profit
with at most k transactions till prices[n].

STATE TRANSITION process
------------------------
At each position, there are two scenarios: sell here or not.
If we sell here, then where to buy before this?

Recurrence relation:
f(n, k) = max(f(i, k - 1) + profit(i + 1, n)), where i = 0, ..., n - 1,
    and profit(i + 1, n) = prices[n] - prices[i + 1].

Two loops i in [0, n], and j in [0, i - 1] gives Cartesian product O(n²).

Complexity
----------
Time O(kn²), where k = 2
Space O(kn)

4. ADD ANOTHER DIMENSION OF STATE to TRADE SPACE FOR TIME! - 3D state

Trade space for time
--------------------
There are two actions to take for each transaction: buy and sell.
Above dynamic programming state transition is O(kn²), because it
needs to iterate all possible positions to BUY the stock in the inner loop.

How about trade space for time a little bit more, to keep track of the
optimal decision w.r.t where to buy stock?

The trick is to:
Add another dimension of state to keep track of the quantity change in profit of
BUY and SELL stock!


Define state
------------
Define 3D state f(n, k, p) as the profit gain within [0, n],
with kₜₕ transitions, to buy if p == 0 or sell, in a QUANTITY CHANGE perspective,

State transition recurrence relation
------------------------------------
    f(n, k, 0) = max(f(n, k, 0), f(n - 1, k - 1, 1) - prices[n]) # buy here
    f(n, k, 1) = max(f(n, k, 1), f(n - 1, k - 1, 0) + prices[n]) # sell here
    # do nothing here is tracked by f(n, k - 1, 1).

The recurrence relation can be traversed in O(nk) time complexity.

Since f(n) only depends on f(n - 1), then the state space usage can be reduced by n.

And the state can be flattened into a 4-tuple quantity change f(n, k = 2):
    (
        optimal quantity change after 1ₛₜ buying here,
        optimal quantity change after 1ₛₜ selling here,
        optimal quantity change after 2nd buying here,
        optimal quantity change after 2nd selling here,
    )

We have to sell before buying again, so we need to update the 4-tuple in reverse order
while scanning the array. In another word, the states must be updated in a
REVERSE TOPOLOGICAL ORDER of the DEPENDENCY GRAPH.

Note that the state must be updated in a reverse order manner to avoid overriding
data dependent on, because the state has dependency on previous ones.

Complexity: O(nk), where k = 2.

################################################################################
FOLLOW UP

1. How to construct the solution?

Similar to longest common subsequence problem, follow the look up table built
with dynamic programming, and search positions where quantity changes.


'''

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # result = self._maxProfitDivideAndConquer(prices)
        # result = self._maxProfitDP2DState(prices)
        result = self._maxProfitDP3DState(prices)

        print(prices, result)

        return result

    def _maxProfitDivideAndConquer(self, prices: list) -> int:
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

    def _maxProfitDP2DState(self, prices: list) -> int:
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
            # FIXME: this inner loop can be eliminated by adding another dimension of state
            # see below solution
            for j in range(1, i): # sell at this time
                f[i][1] = max(f[i][1], prices[i - 1] - prices[j - 1] + f[j - 1][0])
        return f[-1][1]

    def _maxProfitDP3DState(self, prices: list) -> int:
        '''
        Primal 3d state: f(n, k, p), flattened into this:
            STATE =  (
                optimal quantity change after first buying,
                optimal quantity change after first selling,
                optimal quantity change after second buying,
                optimal quantity change after second selling,
            )

        Complexity: O(kn), where k = 2, n is the size of prices list.
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
