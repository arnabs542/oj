#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
53. Maximum Subarray

Total Accepted: 147195
Total Submissions: 384375
Difficulty: Medium
Contributors: Admin

Find the contiguous subarray within an array (containing at least one number) which
has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide
and conquer approach, which is more subtle.
===============================================================================================
SOLUTION:
    dynamic programming.
    Use max_ending_here to denote the sum of maximum subarray ending with current element, then
        max_ending_here = max(max_ending_here + nums[i], nums[i])
    O(n) time complexity.
'''

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSubArrayDP(nums)

    def maxSubArrayDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum, max_ending_here = nums[0], nums[0]
        for i in range(1, n):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_sum = max(max_ending_here, max_sum)
        return max_sum

    # TODO: divide and conquer solution
