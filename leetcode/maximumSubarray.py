#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
53. Maximum Subarray

Total Accepted: 147195
Total Submissions: 384375
Difficulty: Medium
Contributors: Admin

Find the contiguous subarray within an array (containing at least one number) which
has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide
and conquer approach, which is more subtle.

===============================================================================================
SOLUTION:
    Dynamic Programming.

DEFINE STATE:
    max_ending_here: Maximum subarray sum ending here(with current position)

STATE TRANSITION:
    Scan through the array values, computing at each position the MAXIMUM (positive sum)
subarray ENDING AT THAT POSITION.
    This CURRENT subarray is either empty (in which case its sum is zero) or consists of one
more element(current element) than the maximum subarray ENDING AT THE PREVIOUS position. (If
no empty subarray is allowed, current subarray consists of either one element or one more
element than the previous maximum subarray.)

Use max_ending_here to denote the SUM OF MAXIMUM SUBARRAY ENDING AT EACH POSITION, then
max_ending_here = max(max_ending_here + nums[i], nums[i])

Time Complexity:
The runtime complexity of Kadane's algorithm is O(n).

Generalization:
    The algorithm can also be easily modified to keep track of the starting and ending(
two pointers) indices of the maximum subarray.

Because of the way this algorithm uses optimal substructures (the MAXIMUM SUBARRAY ENDING
AT EACH POSITION is calculated in a simple way from a related but smaller and overlapping
subproblem: the maximum subarray ending at the previous position) this algorithm can be
viewed as a simple example of DYNAMIC PROGRAMMING.

'''

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maxSubArrayDP(nums)

    def maxSubArrayDP(self, nums: list) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_so_far, max_ending_here = nums[0], nums[0]
        for i in range(1, n):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_ending_here, max_so_far)
        return max_so_far

    def maxSubArrayDP2(self, nums: list) -> list:
        """
        :type nums: List[int]
        :rtype: list

        Keep track of two pointers: starting and ending indices of the maximum subarray.
        Returning the corresponding subarray.
        """
        n = len(nums)
        max_so_far, max_ending_here = nums[0], nums[0]
        i, begin, end = 0, 0, 1
        for j in range(1, n):
            if max_ending_here <= 0:
                i = j
                max_ending_here = nums[j]
            else:
                max_ending_here += nums[j]

            if max_ending_here >= max_so_far:
                begin = i
                end = j + 1
                max_so_far = max_ending_here

        print('maximum subarray', nums[begin:end])
        return nums[begin:end]

    # TODO: divide and conquer solution

def test():
    solution = Solution()

    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

    assert solution.maxSubArrayDP2([1]) == [1]
    assert solution.maxSubArrayDP2(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [4, -1, 2, 1]

    print('self test passed')

if __name__ == '__main__':
    test()
