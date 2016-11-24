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
    Use max_ending_here to denote the sum of maximum subarray ending with current element, then
        max_ending_here = max(max_ending_here + nums[i], nums[i])
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
        min_ending_here, max_ending_here, max_so_far = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            t = (max_ending_here * nums[i], min_ending_here * nums[i], nums[i])
            max_ending_here, min_ending_here = max(t), min(t)
            max_so_far = max(max_so_far, max_ending_here)
            pass

        print(max_so_far)
        return max_so_far


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
