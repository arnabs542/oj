#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
325. Maximum Size Subarray Sum Equals k

Given an array nums and a target value k, find the maximum length of a subarray that
sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
Can you do it in O(n) time?

==============================================================================================
SOLUTION

1. Naive solution
Exhaust all  sub-arrays, and verify sum, compare the length.

Complexity: O(N²), O(1)

2. Prefix sum with inverted index hash table
Compute the prefix sum, store inverted index <sum, index> in hash table.
Then whether there is a subarray ending with index i sums up to k can be verify by in O(1),
since range sum = difference of prefix sum.

Complexity: O(N), O(N)

'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        result = self._maxSubArrayLenPrefixSum(nums, k)

        print(nums, k, result)

        return result

    def _maxSubArrayLenPrefixSum(self, nums, k):
        n = len(nums)
        # ps = [0 for _ in range(n + 1)]
        ps = 0

        maxLength = 0
        invertedIndex = {0:0}
        for i in range(1, n + 1):
            ps = ps + nums[i - 1]
            s = ps - k
            if s in invertedIndex:
                maxLength = max(maxLength, i - invertedIndex[s])
            if ps not in invertedIndex:
                invertedIndex[ps] = i
        return maxLength

def test():
    solution = Solution()

    nums = []
    k = 3
    assert solution.maxSubArrayLen(nums, k) == 0

    nums = [3]
    k = 3
    assert solution.maxSubArrayLen(nums, k) == 1

    nums = [1, -1, 5, -2, 3] # ps: 0, 1, 0, 5, 3, 6
    k = 3
    assert solution.maxSubArrayLen(nums, k) == 4

    print("self test passed")

if __name__ == '__main__':
    test()
