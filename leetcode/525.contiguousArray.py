#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

525. Contiguous Array
Medium

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

================================================================================
SOLUTION

1. Brute force count

Exhaust all possible combination, O(N²).

Complexity: O(N²)

2. State transition - prefix sum - COUNT AS SUM

Build a prefix sum array. Treat 0 as -1, and treat 1 as 1, then the sum equal to 0
indicates equal number of 0 and 1.

Also, we need a inverted index mapping to store the sum to index relation.

Complexity: O(N), O(N)

"""

class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = self._findMaxLengthPrefixSum(nums)

        print(nums, " => ", result)

        return result

    def _findMaxLengthPrefixSum(self, nums):
        # prefixSum = [0 for _ in range(len(nums) + 1)]
        maxLength = 0
        sum2index = {0 : 0}
        prefixSum = 0
        for i in range(1, len(nums) + 1):
            prefixSum += 1 if nums[i - 1] == 1 else -1
            if prefixSum in sum2index:
                maxLength = max(maxLength, i - sum2index[prefixSum])
            else: sum2index[prefixSum] = i

        return maxLength

def test():
    solution = Solution()

    assert solution.findMaxLength([]) == 0
    assert solution.findMaxLength([0]) == 0
    assert solution.findMaxLength([0, 1]) == 2
    assert solution.findMaxLength([0, 1, 0]) == 2

    print("self test passed!")

if __name__ == '__main__':
    test()
