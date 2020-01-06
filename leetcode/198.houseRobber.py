#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
198. House Robber

Total Accepted: 102042
Total Submissions: 276733
Difficulty: Easy
Contributors: Admin

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security system connected and it will
automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

===============================================================================================
SOLUTION:
    dynamic programming
'''

class Solution(object):

    def rob(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        amount = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            amount[i] = max(amount[i - 1], nums[i - 1] +
                            amount[i - 2] if i >= 2 else 0)

        return amount[-1]
