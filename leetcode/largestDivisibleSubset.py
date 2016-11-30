#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
368. Largest Divisible Subset

Total Accepted: 15381
Total Submissions: 47084
Difficulty: Medium
Contributors: Admin

Given a set of distinct positive integers, find the largest subset such that every
pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

    nums: [1,2,3]

    Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

    nums: [1,2,4,8]

    Result: [1,2,4,8]

==============================================================================================
SOLUTION:
    Dynamic Programming
STATE: largest divisible subset with largest number as the current one.
'''

class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.largestDivisibleSubsetDP(nums)

    def largestDivisibleSubsetDP(self, nums: list) -> list:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums.sort()
        subsets = [None] * len(nums)  # ending here
        largest_set = []
        for i, _ in enumerate(nums):
            s = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(subsets[j]) > len(s):
                    s = subsets[j]
            subsets[i] = s + [nums[i]]
            if len(subsets[i]) > len(largest_set): largest_set = subsets[i]

        print(subsets)
        return largest_set


def test():
    solution = Solution()

    assert solution.largestDivisibleSubset([1, 2, 3]) == [1, 2]
    assert solution.largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]

    print('self test passed')

if __name__ == '__main__':
    test()
