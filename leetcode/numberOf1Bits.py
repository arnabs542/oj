#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
191. Number of 1 Bits

Total Accepted: 120165
Total Submissions: 314478
Difficulty: Easy
Contributors: Admin

Write a function that takes an unsigned integer and returns the number of ’1' bits
it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011,
so the function should return 3.
'''
class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += n & 0x1
            n >>= 1

        return result

def test():
    solution = Solution()

    assert solution.hammingWeight(11) == 3

    print('self test passed')

if __name__ == '__main__':
    test()
