#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
213. House Robber II

Total Accepted: 42883
Total Submissions: 131357
Difficulty: Medium
Contributors: Admin

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place
for his thievery so that he will not get too much attention. This time, all
houses at this place are arranged in a circle. That means the first house is the
neighbor of the last one. Meanwhile, the security system for these houses remain
the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.
===============================================================================================
SOLUTION:
    dynamic programming
'''

class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def rob(nums):
            """
            :type nums: List[int]
            :rtype: int

            sliding array
            """
            amount = [0, 0]
            for i in range(len(nums)):
                amount[0], amount[1] = amount[1], \
                        max(amount[1], nums[i] + amount[0])

            return amount[-1]

        # mind when nums has only one element
        return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))
