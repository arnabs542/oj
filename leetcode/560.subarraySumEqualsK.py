#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
560. Subarray Sum Equals K

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
1. The length of the array is in range [1, 20,000].
2. The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


Hints:

sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.

==============================================================================================
SOLUTION

1. Brute force
Exhaust all possible subarrays, and check sum.

Complexity: O(N³), O(1)

2. Brute force optimization
Calculate the sum incrementally, while increasing the end index.

Complexity: O(N²), O(1)

2. Two pointers?

No clue yet.

3. Prefix sum
Subarray sum, is kind of range sum query, PREFIX SUM may help.

Build the prefix sum array by integrating, and maintain INVERTED INDEX hash table <sum, list<index>>.

Then scan the prefix sum, for each sum s, check whether s-k exists, and corresponding indices.

NOTE: to speed up when only number of solutions is expected, inverted index hash table can only
contain number of indices.

Complexity: O(N), O(N)

FOLLOW UP
================================================================================
1. Subarray sum less than K.
1) Brute force: O(N²)
2) Prefix sum with self balancing binary search tree: O(NlogN).


"""

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = self._subarraySumPrefixSum(nums, k)

        print(nums, k, result)

        return result

    def _subarraySumPrefixSum(self, nums, k):
        n = len(nums)
        result = 0

        ps = [0 for _ in range(n + 1)] # prefix sum
        invertedIndex = defaultdict(list) # inverted index
        invertedIndex[0].append(0)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + nums[i - 1]
            s = ps[i] - k
            result += len(invertedIndex[s])

            invertedIndex[ps[i]].append(i)
            pass

        return result

def test():
    solution = Solution()

    nums = []
    k = 2
    assert solution.subarraySum(nums, k) == 0

    nums = []
    k = 0
    assert solution.subarraySum(nums, k) == 0

    nums = [1, 1, 1]
    k = 2
    assert solution.subarraySum(nums, k) == 2

    nums = [1, 1, 1]
    k = 0
    assert solution.subarraySum(nums, k) == 0

    nums = [1, 1, 1]
    k = 1
    assert solution.subarraySum(nums, k) == 3

    nums = [1, 1, 1]
    k = 3
    assert solution.subarraySum(nums, k) == 1

    nums = [1, 1, 1]
    k = 4
    assert solution.subarraySum(nums, k) == 0

    print("self test passed")

if __name__ == '__main__':
    test()
