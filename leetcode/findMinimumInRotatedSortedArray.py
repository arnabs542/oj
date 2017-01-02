#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
153. Find Minimum in Rotated Sorted Array

Total Accepted: 124880
Total Submissions: 324750
Difficulty: Medium
Contributors: Admin

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

==============================================================================================
SOLUTION:

We always divide the array by 2, and take the range with smaller values.
'''

class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.findMinBinarySearch(nums)
        return self.findMinBinarySearchOpt(nums)

    def findMinBinarySearch(self, nums):
        if len(nums) == 0:
            return
        if nums[0] <= nums[-1]:
            return nums[0]
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if mid and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                high = mid - 1
            else:
                low = mid + 1

    def findMinBinarySearchOpt(self, nums):
        '''
        comparing the middle value with the higher end value

        This is because while we are computing the middle index, the middle index
        is always biased towards to the low end, because of the math floor operation's
        nature:
            floor(n.x) = n, n is integer, and x is in [0, 9]
        If mid = low, then the comparison between low and mid doesn't make sense. To
        avoid that, we compare mid with higher end.
        '''
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] > nums[high]: low = mid + 1
            else: high = mid
        return nums[low]

def test():
    solution = Solution()

    assert solution.findMin([0]) == 0
    assert solution.findMin([0, 1]) == 0
    assert solution.findMin([1, 0]) == 0
    assert solution.findMin([0, 1, 2, 4, 5, 6, 7]) == 0
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([5, 6, 7, 0, 1, 2, 4]) == 0
    assert solution.findMin([6, 7, 0, 1, 2, 4, 5]) == 0

    print('self test passed')

if __name__ == '__main__':
    test()

