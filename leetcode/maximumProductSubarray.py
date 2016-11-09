#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
152. Maximum Product Subarray

Total Accepted: 78420
Total Submissions: 327167
Difficulty: Medium
Contributors: Admin

Find the contiguous subarray within an array (containing at least one number) which
has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
===============================================================================================
SOLUTION:
    dynamic programming.
    Use max_end to denote the sum of maximum subarray ending with current element, then
        max_end = max(max_end + nums[i], nums[i])
    But, two negatives will give positive product, so we need to keep track of a minimum product
of subarray ending here.
    O(n) time complexity.
'''

class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_so_far, max_so_far, max_product = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            t = (max_so_far * nums[i], min_so_far * nums[i], nums[i])
            max_so_far, min_so_far = max(t), min(t)
            max_product = max(max_product, max_so_far)
            pass

        print(max_product)
        return max_product


def test():
    """TODO: Docstring for test.
    :returns: TODO

    """
    solution = Solution()

    assert solution.maxProduct([2, 3, -2, 4]) == 6
    assert solution.maxProduct([2, 3, -2, 4, -5]) == 240
    assert solution.maxProduct([-2, 3]) == 3
    assert solution.maxProduct([-2]) == -2

    print('self test passed')
    pass

test()
