#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
154. Find Minimum in Rotated Sorted Array II

Total Accepted: 66878
Total Submissions: 185549
Difficulty: Hard
Contributors: Admin

Follow up for "Find Minimum in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

==============================================================================================
SOLUTION:

Adaptation on the pruning condition of BINARY SEARCH.

'''

class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) >> 1
            if nums[mid] > nums[high]: low = mid + 1
            elif nums[mid] == nums[high]: high -= 1
            else: high = mid
        return nums[low]

def test():
    solution = Solution()

    assert solution.findMin([0]) == 0
    assert solution.findMin([0, 1, 1]) == 0
    assert solution.findMin([1, 0]) == 0
    assert solution.findMin([1, 1]) == 1
    assert solution.findMin([1, 1, 2, 2]) == 1
    assert solution.findMin([1, 2, 2, 1]) == 1
    assert solution.findMin([1, 2, 2, 1]) == 1
    assert solution.findMin([0, 1, 2, 4, 5, 6, 7]) == 0
    assert solution.findMin([5, 6, 7, 0, 1, 2, 4]) == 0
    assert solution.findMin([6, 7, 0, 1, 2, 4, 5]) == 0
    assert solution.findMin([2, 4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([10, 1, 10, 10, 10]) == 1

    print('self test passed')

if __name__ == '__main__':
    test()
