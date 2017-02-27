#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
41. First Missing Positive

Total Accepted: 81840
Total Submissions: 329619
Difficulty: Hard
Contributors: Admin

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

==============================================================================================
SOLUTION:
What does first in 'first missing positive' mean? It means the SMALLEST.

O(n) time and O(1) space, indicating something like ASSOCIATIVE ARRAY/HASHING/BUCKET.

1. Bucket
Because we are finding the SMALLEST, then we can literally start from the smallest number 1,
and increase the index to check whether the number exists. The array can contain at most n
numbers, so the smallest would be in range [1, n] inclusive.

So an approach would be:
    Scan the array, put the elements in their right bucket/position: nums[i] = i + 1. Then find the
first element in the array whose value is not equal to its index plus 1.
'''

class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Pass 1, move every value to the position of its value
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                src, dest = i, nums[i] - 1
                nums[src], nums[dest] = nums[dest], nums[src]
            else: i += 1

        # Pass 2, find first location where the index doesn't match the value
        i = 0
        while i < len(nums) and nums[i] == i + 1: i += 1

        return i + 1


def test():
    solution = Solution()

    assert solution.firstMissingPositive([]) == 1
    assert solution.firstMissingPositive([3]) == 1
    assert solution.firstMissingPositive([1, 2, 0]) == 3
    assert solution.firstMissingPositive([3, 4, -1, 1]) == 2
    assert solution.firstMissingPositive([3, 4, -1, 1, 1]) == 2

    print('self test passed')

if __name__ == '__main__':
    test()
