#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
26. Remove Duplicates from Sorted Array

Total Accepted: 176024
Total Submissions: 502530
Difficulty: Easy
Contributors: Admin

Given a sorted array, remove the duplicates in place such that each element appear
only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2
respectively. It doesn't matter what you leave beyond the new length.

==============================================================================================
SOLUTION:
    1. Naive solution: scan the array, pop element when we find duplicates. Worst O(n^2)
    2. TWO POINTERS PARTITION algorithm like quick sort. Keep a PARTITION POINT(SPLIT POINT)
that all elements not on the right of it are definitely unique. Initialize it to be -1, then
scan the array, when we found a non-duplicate element, put the value after PARTITION POINT,
and update the PARTITION POINT. O(n)

'''

class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.removeDuplicatesNaive(nums)
        return self.removeDuplicatesPartition(nums)

    def removeDuplicatesNaive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1

        return len(nums)

    def removeDuplicatesPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = -1
        for j in range(0, len(nums)):
            if nums[j] != nums[j - 1] or j == 0:
                i += 1
                nums[i] = nums[j]

        return i + 1


def test():
    solution = Solution()

    assert solution.removeDuplicates([]) == 0
    assert solution.removeDuplicates([1, 1, 2]) == 2
    assert solution.removeDuplicates([1, 1, 1]) == 1
    assert solution.removeDuplicates([1, 2, 3]) == 3

    print('self test passed')

if __name__ == '__main__':
    test()
