#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
219. Contains Duplicate II

Total Accepted: 82244
Total Submissions: 265100
Difficulty: Easy
Contributors: Admin

Given an array of integers and an integer k, find out whether there are two distinct
indices i and j in the array such that nums[i] = nums[j] and the difference between
i and j is at most k.
'''

class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        visit = {}
        for i, num in enumerate(nums):
            if num in visit and i - num[visit] <= k:
                return True
            visit[num] = i

        return False
