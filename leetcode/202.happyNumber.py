#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
202. Happy Number

Total Accepted: 95894
Total Submissions: 248237
Difficulty: Easy
Contributors: Admin

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

================================================================================
SOLUTION

This is a CYCLE DETECTION problem.

1. Naive solution
Check duplicate until sum equal to 1 with HASH TABLE.
Space complexity: O(m).

2. CYCLE DETECTION - Floyd's tortoise and hare algorithm
Space complexity: O(1).

################################################################################
FOLLOW UP
1. Why would there be a CYCLE in such sequence?
The iterated function f is to compute the sum of squares of digits,
inputs and outputs an integer.

The largest positive integer is 2³² - 1 = 4294967296 - 1. So there are
at most 10 digits in an positive integer.

For function f, its domain is [0, 2³² - 1], and its value RANGE is finite,
with upper bound as: 10* 9²=810, since the largest digit is 9.

So function f maps any integer to a finite range [1, 810]. According to
PIGEONHOLE PRINCIPLE, there must be an duplicate in the iterated sequence.
In another word, there must be a loop. And 1 is a special loop containing
only 1 element, where f(1) = 1.

'''

class Solution(object):

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # result = self._isHappyHash(n)
        result = self._isHappyFloydCycleDetection(n)
        print(n, result)

        return result

    def _isHappyHash(self, n):
        visited = {n}
        while n != 1:
            n = int(sum(map(lambda x: int(x) ** 2, str(n)))) # sum of squares of digits
            if n in visited:
                return False
            else:
                visited.add(n)

        print(n, 'is a happy number')
        return True

    def _isHappyFloydCycleDetection(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # DONE: floyd cycle detection algorithm
        def f(x):
            '''returns sum of squares of digits'''
            result = 0
            while x:
                result += (x % 10) ** 2
                x //= 10
            return result
        slow = f(n)
        fast = f(slow)
        while fast not in (1, slow):
            slow = f(slow)
            fast = f(f(fast))
        return fast == 1

    def _isHappyMathClosedForm(self, n):
        # TODO: closed form mathematical solution?
        pass


def test():
    solution = Solution()

    assert solution.isHappy(1)
    assert solution.isHappy(19)

if __name__ == '__main__':
    test()
