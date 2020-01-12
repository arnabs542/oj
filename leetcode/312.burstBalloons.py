#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
312. Burst Balloons
Hard

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.

================================================================================
SOLUTION

1. Brute force - permutation - depth first search

Exhaust all permutations, and perform forward state transition to compute gain,
take the maximum.

Forward state transition means bursting balloons one by one.

Define state: (
    partial permutation,
    next permutation position,
    available candidates,
)

Complexity: O(n²n!)

There are P(n, n) = n! permutations, for each permutation, it takes O(n²)
complexity to compute the gain.

2. Brute force - combination - depth first search with memoization
Lots of duplicates are involved in permutations.

In this graph, vertices are the balloons set, and edges are balloons.
Following an edge means bursting a balloon, and it'll lead to next state,
a subset of current vertex set.

Though vertices are represented by set, there are overlapping problems.
For example, 12345 and 21345 have subproblem 345 overlapping.

So it makes sense to memoize states given by vertices set.

Complexity
There are \sum_k{C(n,k)}=2ⁿ combination subsets, so the complexity is: O(n2ⁿ).
Upper bound for n is 500, giving upper bound O(2⁵⁰⁰), infeasible!

3. Divide and conquer
If we choose a balloon to burst first, then the remaining balloons are not
ideally partitioned in a way that they don't interleave or affect each other.

Actually, the remaining balloons are represented by a subset C(n, k).
This is the above combination situation.

Is there such perspective that the problem can be divided into two
independent partitions?

4. BACKWARD INDUCTION - dynamic programming - RANGE STATE - Cartesian product

Forward induction encounters some severe problem:
After bursting a balloon, the state transition recurrence relation is
still with respect to set, the vertices set, giving 2ⁿ subsets.

State represented by combinatorial sets are not easily tractable,
involving combination subsets, a.k.a, exponential complexity.

--------------------------------------------------------------------------------
BACKWARD INDUCTION

But, what if we deduce BACKWARD?!

Instead of divide the problem by the FIRST balloon to burst, we divide the problem
by the LAST balloon to burst, at each step.
Then the problem is partitioned into two subproblems, defined on two
INDEPENDENT sections. The front section and back section must be cleared
before the LAST one, so they have a well defined BOUNDARY and don't affect
each other. And each of them can be REPRESENTED with an RANGE STATE!

Then the state transition is regarding to two ends ranges.

Define two dimensional state dp[i][j] indicates maximum gain that can be
obtained from subarray in range [i, ..., j].
Then we make choice about which balloon to burst last.

The recurrence relation is given by:
    dp[i][j] = max{dp[i][k-1] + dp[k+1][j] + gain(k) | k=i, i+1, ..., j},
    gain(k) = nums[i-1] * nums[k] * nums[j+1],

Current state(i, j) depends on (i, k-1) and (k+1, j), then we can adopt
reversal row major bottom up fashion to build the table.

Complexity: O(N³)

"""

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = self._maxCoinsDp(nums)

        print(nums, " => ", result)

        return result

    def _maxCoinsDp(self, nums):
        n = len(nums)
        # initialization
        dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

        for s in range(n - 1, -1, -1): # starting index
            for e in range(s, n):  # ending index
                for last in range(s, e + 1): # choose one as the last to burst
                    gain = (nums[s-1] if s else 1) * nums[last] * (nums[e+1] if e < n-1 else 1)
                    dp[s][e] = max(dp[s][e], dp[s][last-1] + dp[last+1][e] + gain) # recurrence relation

        return dp[0][n-1] if n else 0

def test():
    solution = Solution()

    assert solution.maxCoins([]) == 0
    assert solution.maxCoins([0]) == 0
    assert solution.maxCoins([1]) == 1
    assert solution.maxCoins([1, 1]) == 2
    assert solution.maxCoins([3, 1, 5, 8]) == 167
    assert solution.maxCoins([3, 1, -5, 8]) == 56
    # assert solution.maxCoins([3, 1, 5, 8]) == 167

    print("self test passed!")

if __name__ == '__main__':
    test()

