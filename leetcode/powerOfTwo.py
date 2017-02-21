#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
231. Power of Two

Total Accepted: 112743
Total Submissions: 288297
Difficulty: Easy
Contributors: Admin

Given an integer, write a function to determine if it is a power of two.

==============================================================================================
SOLUTION:

1. Brute-force method: keep dividing
2. Use Bit manipulation: n & (n - 1) == 0 if n is power of 2.

'''

class Solution(object):

    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.isPowerOfTwoBit(n)

    def isPowerOfTwoBit(self, n):
        return n and n & (n - 1) == 0


def test():
    solution = Solution()

    assert not solution.isPowerOfTwo(0)
    assert solution.isPowerOfTwo(1)
    assert solution.isPowerOfTwo(2)
    assert not solution.isPowerOfTwo(3)
    assert solution.isPowerOfTwo(1 << 16)

    print('self test passed')

if __name__ == '__main__':
    test()
