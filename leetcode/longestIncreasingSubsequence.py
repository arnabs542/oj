#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
300. Longest Increasing Subsequence

Total Accepted: 56604
Total Submissions: 152709
Difficulty: Medium
Contributors: Admin

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note
that there may be more than one LIS combination, it is only necessary for you to return
the length.

Your algorithm should run in O(n²) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

==============================================================================================
SOLUTION:

1. Dynamic Programming:
Define state f(i): longest increasing subsequence ending here.
f(i) = max(f(j) + 1), where nums[i] > nums[j], j = 1, ..., i - 1

Time complexity: O(N²).

2. Logarithmic solution.
'''

class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.lengthOfLISDP(nums)

    def lengthOfLISDP(self, nums: list) -> int:
        f = [1] * (len(nums) + 1)
        f[0] = 0
        len_lis = 0
        for i in range(1, len(nums) + 1):
            for j in range(1, i):
                # if statement here will be faster than logic expression
                if nums[i - 1] > nums[j - 1]:
                    f[i] = max(f[i], f[j] + 1)
            len_lis = max(len_lis, f[i])

        # print(f, len_lis)
        return len_lis

    # TODO: log solution

def test():
    solution = Solution()

    assert solution.lengthOfLIS([]) == 0
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6

    print('self test passed')

if __name__ == '__main__':
    test()
