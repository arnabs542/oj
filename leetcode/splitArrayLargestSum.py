#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
410. Split Array Largest Sum
Hard


Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],

================================================================================
SOLUTION

1. Brute force - combination

Complexity: O(C(n, m)n).

2. Dynamic programming - Cartesian product

Since different combinations have overlapping subproblems.

Define state as a tuple of:
    (
    m: m subarrays,
    n: size of array,
    )
representing the optimal solution at the condition (m, n).

Then we have recurrence relation:
    dp[m][n] = min_x{
        max(sum(x, ..., n), dp[m - 1][x - 1])
        | x in [m, n]
    }

Complexity: O(mn²n) = O(mn³)

--------------------------------------------------------------------------------
Optimization

1) Prefix sum
It's not O(mn²) because summing subarray is O(n).
Build a prefix sum array will reduce that!

2) Early stop
The cumulative sum, or prefix sum, is increasing, which means we can stop early!

3) Binary search
Integers are non-negative, which means the prefix sum is monotonically increasing!
Sorted prefix sum means we can use binary search.
Complexity: O(mnlogn)

"""

from _decorators import timeit


class Solution(object):
    @timeit
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # result = self._splitArrayDpNaive(nums, m)
        # result = self._splitArrayDpPrune(nums, m)
        result = self._splitArrayDpBinarySearch(nums, m)

        print(nums, m, " => ", result)

        return result

    def _splitArrayDpNaive(self, nums, m):
        n = len(nums)
        if not 1 <= m <= n: return 0
        dp = [[sum(nums[:j]) if i == 1 else float('inf') for j in range(n + 1)] for i in range(m + 1)]

        for i in range(2, m + 1): # 2
            for j in range(i, n + 1): # 2
                for k in range(j, i - 1, -1): # 1
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k - 1], sum(nums[k - 1:j])))
                pass

        return dp[m][n]

    def _splitArrayDpPrune(self, nums, m):
        n = len(nums)
        if not 1 <= m <= n: return 0
        dp = [[sum(nums[:j]) if i == 1 else float('inf') for j in range(n + 1)] for i in range(m + 1)]

        for i in range(2, m + 1): # 2
            for j in range(i, n + 1): # 2
                s = 0
                for k in range(j - 1, i - 2, -1): # 1
                    # DONE: binary search is faster, see below
                    s += nums[k]
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], s))
                    if s >= dp[i - 1][k]: break # early stop
                pass

        return dp[m][n]

    def _splitArrayDpBinarySearch(self, nums, m):
        n = len(nums)
        if not 1 <= m <= n: return 0
        prefixSum = [0 for i in range(n + 1)]
        for i in range(1, n + 1): prefixSum[i] = prefixSum[i-1] + nums[i-1]

        dp = [prefixSum[j] - prefixSum[0] for j in range(n + 1)] # one dimensional state

        for i in range(2, m + 1): # 2
            for j in range(n, i - 1, -1): # reverse order! 2
                low, high = i - 1, j - 1 # index range
                while low <= high: # DONE: binary search on monotonic array
                    mid = (low + high) // 2
                    s = prefixSum[j] - prefixSum[mid]
                    dp[j] = min(dp[j], max(dp[mid], s))

                    if s > dp[mid]: low = mid + 1
                    elif s < dp[mid]: high = mid - 1
                    else: break

        return dp[n]

    # TODO: even more efficient binary search solution?

def test():
    solution = Solution()

    assert solution.splitArray([], 0) == 0
    assert solution.splitArray([], 1) == 0
    assert solution.splitArray([1], 1) == 1
    assert solution.splitArray([1, 1], 1) == 2
    assert solution.splitArray([1, 1], 2) == 1
    assert solution.splitArray([1, 1], 3) == 0
    assert solution.splitArray([1, 1, 1], 3) == 1
    assert solution.splitArray([7, 2, 5, 10, 8], 2) == 18
    assert solution.splitArray([7, 2, 5, 10, 8], 3) == 14
    assert solution.splitArray([7, 2, 5, 10, 8], 4) == 10
    assert solution.splitArray([700000000, 200000000, 500000000, 1000000000, 800000000], 2)
    assert solution.splitArray([1,4,4], 3) == 4

    print("self test passed!")

if __name__ == "__main__":
    test()
