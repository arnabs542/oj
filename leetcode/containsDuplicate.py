#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
217. Contains Duplicate

Total Accepted: 123554
Total Submissions: 287862
Difficulty: Easy
Contributors: Admin

Given an array of integers, find if the array contains any duplicates. Your function
should return true if any value appears at least twice in the array, and it should
return false if every element is distinct.
'''

class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
