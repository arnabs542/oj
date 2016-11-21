#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
27. Remove Element

Total Accepted: 157415
Total Submissions: 431922
Difficulty: Easy
Contributors: Admin

Given an array and a value, remove all instances of that value in place and
return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

Hint:

Try two pointers.
Did you use the property of "the order of elements can be changed"?
What happens when the elements to remove are rare?

==============================================================================================
SOLUTION:
    TWO POINTERS PARTITIONING ALGORITHM.
    Because the elements to remove can be rare, so we put the SPLIT POINT at the right part of
the array and only swap elements equal to the target value to the right part(elements from
the SPLIT POINT to right are all equal to the target element).

'''

class Solution(object):

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = len(nums), 0
        while j < i and j < len(nums):
            if nums[j] == val:
                i -= 1
                nums[j], nums[i] = nums[i], nums[j]
            else:
                j += 1

        print(nums)
        return i

def test():
    solution = Solution()

    assert solution.removeElement([], 0) == 0
    assert solution.removeElement([1, 1, 2], 2) == 2
    assert solution.removeElement([1, 1, 1], 1) == 0
    assert solution.removeElement([1, 2, 3], 2) == 2
    assert solution.removeElement([3, 2, 2, 3], 3) == 2

    print('self test passed')

if __name__ == '__main__':
    test()
