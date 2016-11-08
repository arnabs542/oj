#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
278. First Bad Version

Total Accepted: 70505
Total Submissions: 294330
Difficulty: Easy
Contributors: Admin

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of
calls to the API.
===============================================================================================
SOLUTION:
    BINARY SEARCH
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) >> 1
            if isBadVersion(mid):
                high = mid - 1
            elif not isBadVersion(mid):
                low = mid + 1
        return max(low, high)
