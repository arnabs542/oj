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
    Dynamic Programming.

    Scan through the array values, computing at each position the maximum (positive sum) subarray
ENDING AT THAT POSITION.

    This CURRENT subarray is either empty (in which case its sum is zero) or consists of one more
element(current element) than the maximum subarray ENDING AT THE PREVIOUS position. (If no empty
subarray is allowed, current subarray consists of either one element or one more element than the
previous maximum subarray.)

    Use max_ending_here to denote the SUM OF MAXIMUM SUBARRAY ENDING AT EACH POSITION, then
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
        max_so_far, max_ending_here = nums[0], nums[0]
        for i in range(1, n):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far

    # TODO: divide and conquer solution
