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

==============================================================================================
SOLUTION

1. Brute force
Enumerate all windows of length k, check duplicate in the window. Then this is reduced to problem I.

Complexity: O(nk), O(k).

2. State transition - hash set

The brute force method above involves duplicate computation.
And it can be eliminated by utilizing the state transition while sliding windows.

Maintain a hash set with size k.

Complexity: O(n), O(k)

3. Inverted index
Similar to above solution, but using inverted index to tackle the constraint of window size k.

Complexity: O(n), O(n)

'''

class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        return self._containsNearbyDuplicateInvertedIndex(nums, k)

    def _containsNearbyDuplicateInvertedIndex(self, nums, k):
        visit = {}
        for i, num in enumerate(nums):
            if num in visit and i - num[visit] <= k:
                return True
            visit[num] = i

        return False
