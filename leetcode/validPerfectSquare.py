#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
367. Valid Perfect Square

Total Accepted: 24338
Total Submissions: 65503
Difficulty: Medium
Contributors: Admin

Given a positive integer num, write a function which returns True if num is a perfect
square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

==============================================================================================
SOLUTION:
1. Find and check.

Find round square root integer, check its square equivalence with target number.
Square root finding can be solved with binary search or Newton's method

Time Complexity: O(logN).

2. Verify with square numbers' properties

Square number can be written as first n odd numbers.
Refer to https://en.wikipedia.org/wiki/Square_number#Properties

Proof:
    n ^ 2 = (n − 1) ^ 2 + (n − 1) + n = (n − 1) ^ 2 + (2n − 1) = ...

Time complexity: O(sqrt(N))
'''

class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # return self.isPerfectSquareNewton(num)
        # return self.isPerfectSquareBS(num)
        return self.isPerfectSquareDecomposition(num)

    def isPerfectSquareNewton(self, num: int) -> bool:
        x = num
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num

    def isPerfectSquareDecomposition(self, num: int) -> bool:
        '''
        square number = 1 + 3 + 5 + ... ?
        '''
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0

    def isPerfectSquareBS(self, num: int) -> bool:
        '''
        binary search
        '''
        low, high = 0, num
        while low <= high:
            root = (low + high) // 2
            if root * root > num:
                high = root - 1
            elif (root + 1) ** 2 <= num:
                low = root + 1
            else:
                break
        print(root, num)
        return root * root == num

def test():
    solution = Solution()

    assert solution.isPerfectSquare(0)
    assert solution.isPerfectSquare(1)
    assert solution.isPerfectSquare(16)
    assert not solution.isPerfectSquare(14)
    assert not solution.isPerfectSquare(26)
    assert solution.isPerfectSquare(25)

    print('self test passed')

if __name__ == '__main__':
    test()
