#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
35. Search Insert Position

Total Accepted: 129880
Total Submissions: 336132
Difficulty: Medium
Contributors: Admin

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

SOLUTION
================================================================================

This is to find lower bound position in a sorted array.
Use binary search!

'''

class Solution(object):

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        """
        return self.searchInsertBinarySearch(nums, target)

    def searchInsertBinarySearch(self, nums, target):
        """
        Binary search
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return low

def test():
    solution = Solution()

    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0

    print('self test passed')

if __name__ == '__main__':
    test()
