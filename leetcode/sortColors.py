#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
75. Sort Colors

Total Accepted: 129346
Total Submissions: 355241
Difficulty: Medium
Contributors: Admin

Given an array with n objects colored red, white or blue, sort them so that objects
of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue
respectively.

Note:
You are not suppose to use the library's sort function for this problem.

==============================================================================================
SOLUTION:
    This is exactly the Dutch National Flag problem, two pointers for three-way partition!
Choose a pivot value, say it's 1, and use two pointers smaller, greater on the left, right
respectively.
    smaller: elements on the left of it are smaller than pivot.
    greater: elements on the right of it are greater than the pivot.

    Then scan the list from left to right, swap smaller elements to the left, greater elements
to the right, updating the splitting two pointers as well.
'''

class Solution(object):

    def sortColors(self, nums: list):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        beats 97.36%, 2016-11-24 14:17
        """
        pivot = 1
        smaller, greater = 0, len(nums) - 1
        i = 0
        while i <= greater:
            if nums[i] < pivot:
                nums[smaller], nums[i] = nums[i], nums[smaller]
                smaller += 1
                i += 1
            elif nums[i] > pivot:
                nums[greater], nums[i] = nums[i], nums[greater]
                greater -= 1
            else:
                i += 1
            pass
        print(smaller, greater, nums)
        return nums

def test():
    solution = Solution()

    l = []
    assert solution.sortColors(l) == sorted(l)

    l = [1]
    assert solution.sortColors(l) == sorted(l)

    l = [2, 0]
    assert solution.sortColors(l) == sorted(l)

    l = [2, 2, 0, 0, 1, 1, 1, 2]
    assert solution.sortColors(l) == sorted(l)

    print('self test passed')

if __name__ == '__main__':
    test()
