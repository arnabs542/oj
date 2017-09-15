#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
398. Random Pick Index

Total Accepted: 13732
Total Submissions: 33844
Difficulty: Medium
Contributors: Admin

Given an array of integers with possible duplicates, randomly output the index of a given
target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal
// probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

==============================================================================================
SOLUTION

This is a stochastic process.

1. Reservoir sampling, refer to '382. Linked List Random Node'.

2. Preprocess the input numbers into a list of tuples (value, index). O(nlogn)
And binary search for the bound item, O(logn)
Generate a random number, O(1)

'''

import random

class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idx_pick = -1
        idx_target = -1
        for i, n in enumerate(self.nums):
            if n != target:
                continue
            # sample
            r = random.randint(0, idx_target + 1)
            if r < 1:
                idx_pick = i
            idx_target += 1
        return idx_pick



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
