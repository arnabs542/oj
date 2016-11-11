#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
238. Product of Array Except Self

Total Accepted: 69988
Total Submissions: 151717
Difficulty: Medium
Contributors: Admin

Given an array of n integers where n > 1, nums, return an array output such that output[i]
is equal to the product of all the elements of nums except nums[i].

Solve it WITHOUT DIVISION and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as
extra space for the purpose of space complexity analysis.)
===============================================================================================
SOLUTION:
    product[i] = left * right = \prod{j=0}^{i-1} * \prod{j=i+1}^{n-1}
    product[i+1] = left * right = \prod{j=0}^{i} * \prod{j=i+2}^{n-1}
    ...

    Scan the array forward and backward to respectively accumulate the product of elements on
the left and right of ith element.
'''
class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = [1] * (len(nums))
        left = right = 1
        for i in range(len(nums)):
            product[i] *= left
            left *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            product[i] *= right
            right *= nums[i]
            pass

        print(product)
        return product


def test():
    solution = Solution()

    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    print('self test passed')

test()
