#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
354. Russian Doll Envelopes
Hard

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

================================================================================
SOLUTION

1. Depth first search - permutation

Complexity: O(\sum_k{P(n, k)})

2. Depth first search - combination

Does the optimal solution present ORDER INVARIANT?
Obviously, it does.

Sort the array, and try every possible combination.

Define state as a tuple:
    (
        i: beginning index array
    )

Complexity O(2ⁿ)

--------------------------------------------------------------------------------
Combination subsets to Cartesian product with memoization

3. Dynamic programming - longest increasing subsequence

Combination subsets involves overlapping subproblems. The exponential
complexity can be reduced to Cartesian product by eliminating the
overlapping subproblems.

Treat this a longest increasing subsequence problem!

Define state dp[i] as the longest increasing subsequence ending here.

Complexity: O(N²)

4. Longest common subsequence

Sort the envelopes using width as key, producing sorted list l1.
Sort the envelopes using height as key, producing sorted list l2.

The longest common subsequence is the maximum number of envelopes.

Complexity: O(N²)

4. Dynamic programming optimized with binary search - reduce to one dimensional LIS
Well, this is apparently LIS(longest increasing subsequence).

And after sorting according to width, only one dimension need to be considered.
So, this is REDUCED TO ONE DIMENSIONAL LIS already.

One problem with envelopes of same width, [2, 3] can't fit into [2, 4],
so it can't be considered as increasing sequence.

The trick is to sort the array ascending on width and descending on height.
So that [2, 4] comes first than [2, 3].

Now one dimensional LIS problem can be solved with dynamic programming with
BINARY SEARCH FOR LOWER BOUND.

5. Greedy strategy - Don't have one...

Put the smaller one into a lower bound larger envelope.

The problem is, however, how to define small?
This is a problem with two dimensional elements!

Among [1, 5], [2, 4], [3, 5], which is smaller? 2 > 1 but [2, 4] can fit
into [3, 5] while [1, 5] can't.

"""

from _decorators import timeit

import bisect

class Solution(object):
    @timeit
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # result = self._maxEnvelopesDp(envelopes)
        # result = self._maxEnvelopesDpBinarySearch(envelopes)
        result = self._maxEnvelopesDpBinarySearchOpt(envelopes)

        print(envelopes, result)

        return result

    def _maxEnvelopesDp(self, envelopes):
        envelopes.sort()
        dp = [1 if i else 0 for i in range(len(envelopes) + 1)]
        l = 1 if envelopes else 0

        for i, envelope in enumerate(envelopes):
            for j in range(i):
                if not (envelopes[j][0] < envelope[0] and envelopes[j][1] < envelope[1]):
                    continue
                dp[i + 1] = max(dp[i + 1], dp[j + 1] + 1)
                l = max(l, dp[i + 1])
        return l

    def _maxEnvelopesDpBinarySearch(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [[-1, -1] for i in range(len(envelopes) + 1)]
        l = 0

        for i, envelope in enumerate(envelopes):
            low, high = 0, l
            while low <= high:
                mid = (low + high) // 2
                if  dp[mid][1] < envelope[1]: low = mid + 1
                else: high = mid - 1 # search lower bound
            if low > l:
                dp[low] = envelope
                l = low
            elif envelope[1] < dp[low][1]:
                dp[low] = envelope

        return l

    def _maxEnvelopesDpBinarySearchOpt(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [-1 for i in range(len(envelopes) + 1)]
        l = 0

        for _, envelope in enumerate(envelopes):
            low, high = 0, l
            while low <= high:
                mid = (low + high) // 2
                if  dp[mid] < envelope[1]: low = mid + 1
                else: high = mid - 1 # search lower bound
            if low > l:
                dp[low] = envelope[1]
                l = low
            elif envelope[1] < dp[low]:
                dp[low] = envelope[1]

        return l


def test():
    solution = Solution()

    assert solution.maxEnvelopes([]) == 0
    assert solution.maxEnvelopes([[1, 2]]) == 1
    assert solution.maxEnvelopes([[1, 2], [3, 4]]) == 2
    assert solution.maxEnvelopes([[1, 7], [3, 4], [4, 5]]) == 2
    assert solution.maxEnvelopes([[1, 7], [3, 4], [3, 8]]) == 2

    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    assert solution.maxEnvelopes(envelopes) == 3

    import yaml
    with open("./russianDollEnvelopes.json", "r") as f:
        data = yaml.load(f)

    for r in data:
        assert solution.maxEnvelopes(r['input']) == r['output']


    print("self test passed!")

if __name__ == '__main__':
    test()
