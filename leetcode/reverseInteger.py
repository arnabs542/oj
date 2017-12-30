#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

==============================================================================================
SOLUTION

For positive numbers, process it from least significant position to most significant.
And the least significant digit can be obtained by modulo by 10.

There are negative numbers, change it to positive first, since -3 % 10 = 7, not 3.

And how to detect overflow?
The valid range is [-2³¹, 2³¹ - 1]

"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = self._reverse(x)

        print(x, result)

        return result

    def _reverse(self, x):
        sign = 1 if x >= 0 else -1
        x *= sign
        y = 0
        while x:
            x, r = divmod(x, 10)
            y = 10 * y + r
        y *= sign
        if not -(1<<31) <= y <= (1<<31) - 1:
            return 0
        return y

def test():
    solution = Solution()

    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(-120) == -21
    assert solution.reverse(2147483648) == 0 # 2 ** 31, overflow

    print("self test passed")

if __name__ == '__main__':
    test()
