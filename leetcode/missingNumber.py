#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
268. Missing Number

Total Accepted: 80861
Total Submissions: 187716
Difficulty: Medium
Contributors: Admin

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the
one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using
only constant extra space complexity?

==============================================================================================
SOLUTION:
    1. Hash table to store all distinct numbers from 0, 1, ..., n. Remove one by one while
scanning the list. Complexity: time O(n), space O(n).
    2. Since numbers are distinct, and only one is missing. We could find the number by subtract
the total sum from 0 to n by the sum of given array. Then the difference is the missing number.
    3. Bit manipulation(XOR).
Taking another sequence of integers from 0 to n, then the missing value is the SINGLE one.
Because (0^0) ^ (1^1) ^ ... ^ (n ^ n) = 0, if one is missing, then the XOR result is the
missing value.
'''

class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.missingNumberSum(nums)
        return self.missingNumberXOR(nums)

    def missingNumberSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        s = n * (n + 1) / 2
        return s - sum(nums)

    def missingNumberXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = 0
        for i, num in enumerate(nums):
            xor ^= i + 1 ^ num
        return xor

def test():
    solution = Solution()

    assert solution.missingNumber([0]) == 1
    assert solution.missingNumber([0, 1, 3]) == 2

    print('self test passed')

if __name__ == '__main__':
    test()
