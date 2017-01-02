#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
33. Search in Rotated Sorted Array

Total Accepted: 137787
Total Submissions: 432668
Difficulty: Hard
Contributors: Admin

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

==============================================================================================
SOLUTION

Adapted Binary search, with more cases.
'''

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[high]:  # two cases
                if nums[mid] < target <= nums[high]:  # different range
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            pass
        return -1

def test():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 2) == 6
    assert Solution().search([5, 1, 2, 3, 4], 1) == 1
    assert Solution().search([5, 6, 7, 8, 9, 1, 2, 3, 4], 2) == 6

    print("self test passed")

if __name__ == "__main__":
    test()
