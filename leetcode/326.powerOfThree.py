#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
326. Power of Three

Total Accepted: 76130
Total Submissions: 194697
Difficulty: Easy
Contributors: Admin
Given an integer, write a function to determine if it is a power of three.


Follow up:
Could you do it without using any loop / recursion?

==============================================================================================
SOLUTION:

1. Keep dividing by 3
Complexity: O(logN)

2. Logarithm
If n is power of three, log₃(n) is integer.
log₃(n) = ln(n)/ln(3).

Complexity: O(logN)

3. Lookup table

Write down the look up table, 3, 9, 27, 81, ...

Complexity: O(logN) or O(1)


'''

class Solution(object):

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return self.isPowerOfThreeDivide(n)
        return self.isPowerOfThreeLog(n)

    def isPowerOfThreeDivide(self, n) -> bool:
        while n > 1 and n % 3 == 0:
            n //= 3
        return n == 1

    def isPowerOfThreeLog(self, n) -> bool:
        import math
        return n and math.log(n, 3).is_integer()

    # TODO: check modulo of maximum power of 3 integer

def test():
    solution = Solution()

    assert not solution.isPowerOfThree(0)
    assert solution.isPowerOfThree(1)
    assert not solution.isPowerOfThree(12)
    assert solution.isPowerOfThree(27)

    print("self test passed")

if __name__ == '__main__':
    test()
