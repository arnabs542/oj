#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
581. Shortest Unsorted Continuous Subarray
Easy


Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.

================================================================================
SOLUTION

1. Brute force
Exhaust all subarrays [i, ..., j], check front and back parts, [0, ..., i - 1],
and [j + 1, ..., n] sorted or not.

Complexity: O(N³)

2. Sort
Stable sort, and match leading increasing and trailing decreasing subarray greedily.
In another word, sort the indices, and find first and last indices that aren't
in the supposed position!

Complexity: O(nlogn)

3. Maximum/minimum analysis: left and right arrays

What does this unsorted continuous subarray mean?
After sorting, it will fit into the sorted array, which means, in this subarray,
the minimum and maximum must fit into the sorted array!

The minimum of the continuous unsorted subarray must violates the sorted condition:
    minimum of it is no less than left elements,
    maximum of it is no greater than right elements,

Complexity: O(n)

4. Stack?

5. Stack without extra space?

"""

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = self._findUnsortedSubarraySort(nums)
        result = self._findUnsortedSubarrayExtrema(nums)

        print(nums, " => ", result)

        return result

    def _findUnsortedSubarraySort(self, nums):
        indices = list(range(len(nums)))
        indices.sort(key=lambda x: (nums[x], x)) # force stable sort, adding index as second key

        i = 0
        while i < len(nums) and i == indices[i]: i += 1
        j = len(nums) - 1
        while j >= 0 and j == indices[j]: j -= 1

        return max(0, j - i + 1)

    def _findUnsortedSubarrayExtrema(self, nums):
        mins = [float('inf') for _ in range(len(nums))] # minimum in range [i, ..., n]
        maxs = [float('-inf') for _ in range(len(nums))] # maximum in range [0, ..., i]
        for i in range(len(nums) - 1, -1, -1):
            mins[i] = min(mins[i + 1] if i < len(nums) - 1 else float('inf'), nums[i])
        for i in range(len(nums)):
            maxs[i] = max(maxs[i - 1] if i else float('-inf'), nums[i])

        # print(mins, maxs)
        i, j = 0, len(nums) - 1
        while i < len(nums) and nums[i] <= mins[i]: i += 1
        while j >= 0 and nums[j] >= maxs[j]: j -= 1

        return max(0, j - i + 1)

    # TODO: stack, constant space usage

def test():
    solution = Solution()

    assert solution.findUnsortedSubarray([]) == 0
    assert solution.findUnsortedSubarray([1]) == 0
    assert solution.findUnsortedSubarray([1, 2]) == 0
    assert solution.findUnsortedSubarray([2, 1]) == 2
    assert solution.findUnsortedSubarray([1, 2, 1]) == 2
    assert solution.findUnsortedSubarray([2, 1, 1]) == 3
    assert solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert solution.findUnsortedSubarray([2, 6, 8, 10, 4, 9, 15]) == 5

    print("self test passed!")

if __name__ == '__main__':
    test()
