#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
476. Number Complement

Total Accepted: 15202
Total Submissions: 25027
Difficulty: Easy
Contributors: love_FDU_llp

Given a positive integer, output its complement number. The complement strategy is to flip
the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement
is 010. So you need to output 2.

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement
is 0. So you need to output 0.


==============================================================================================
SOLUTION

1. Close-form solution
Denote a number by d, assume d is of n bits. Then:
    d = aₙ 2ⁿ-¹ + ... + a₀ 2⁰
The complement number d' is:
    d'= (1 - aₙ) 2ⁿ-¹ + ... + (1 - a₀) 2⁰
      = (2⁰ + ... + 2ⁿ-¹) - d
      = 2ⁿ - d - 1

2. Use (2ⁿ - 1) ^ d

'''

class Solution(object):

    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.findComplementBit(num)

    def findComplementBit(self, num):
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num

def test():
    solution = Solution()

    assert solution.findComplement(5) == 2
    assert solution.findComplement(1) == 0

    print("self test passed")

if __name__ == '__main__':
    test()
