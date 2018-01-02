#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
646. Maximum Length of Pair Chain

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].

================================================================================
SOLUTION

1. Brute force - permutation

Of course not..

Complexity: O(n!2ⁿ)

2. Brute force - combination
Sort and make binary decision for each pair.

Complexity: O(2ⁿ)

3. Dynamic programming

Define state dp[n] as longest chain  which can be formed with n sorted pairs.

Complexity: O(nlogn) + O(n²)

4. Greedy strategy

The items have same value gain 1, there is a greedy strategy.

Sort, and for each overlapping pair, take the one with shortest second number.

Complexity: O(nlogn)

"""

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        result = self._findLongestChainGreedy(pairs)

        print(pairs, 'result: ', result)

        return result

    def _findLongestChainGreedy(self, pairs):
        pairs.sort()
        end = float('-inf')
        result = 0
        for pair in pairs:
            if pair[0] > end:
                result += 1
                end = pair[1]
            else:
                end = min(pair[1], end)
        return result


def test():
    solution = Solution()

    assert solution.findLongestChain([]) == 0
    assert solution.findLongestChain([[1, 2]]) == 1
    assert solution.findLongestChain([[1, 2], [2, 3]]) == 1
    assert solution.findLongestChain([[1, 2], [2, 3], [3, 4]]) == 2

    print("self test passed!")

if __name__ == '__main__':
    test()
