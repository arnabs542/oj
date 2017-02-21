#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
371. Sum of Two Integers

Total Accepted: 52044
Total Submissions: 101186
Difficulty: Easy
Contributors: Admin

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

==============================================================================================
SOLUTION

There are only four cases in bit addition,
0+0=0
0+1=1
1+0=1
1+1=10 (and generates carry)

The OR operation handles the first three cases. The last case contains carry bit.

1. RECURSIVE RELATION!
Take XOR operation to get a base sum, then use AND to get the carry bits. Shift the carry
bits leftward by 1. Recursively calculate the sum of carry number and the base sum until
carry is zero.

Refer to the c++ implementation, for Python's integers have no upper bound.


'''

class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        s =  self.getSumRecursive(a, b)
        print( a, '+', b, '=', s)
        return s

    def getSumRecursive(self, a, b):
        # FIXME: for python, integer numbers seem not to be represented in
        # 2's complement number system. Thus 1 << n goes towards infinity with n.
        if b == 0 or b >= 1 << 31:
            return a
        s = a ^ b
        carry = ((a & b) << 1) & 0xFFFFFFFF
        print('%x' % (carry))
        return self.getSumRecursive(s, carry)

def test():
    solution = Solution()

    assert solution.getSum(1, 2) == 3
    assert solution.getSum(0b1111, 0b0100) == 0b10011
    assert solution.getSum(-1, 10) == 9

    print("self test passed")

if __name__ == '__main__':
    test()
