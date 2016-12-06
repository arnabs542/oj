#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
365. Water and Jug Problem

Total Accepted: 9652
Total Submissions: 37463
Difficulty: Medium
Contributors: Admin

You are given two jugs with capacities x and y litres. There is an infinite amount of
water supply available. You need to determine whether it is possible to measure exactly
z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one
or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug
itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

==============================================================================================
SOLUTION:
    If z is measurable, then z = ax + by, which is the form of Bézout's identity.
Denote the greatest common divisor of x and y with d, then there exist such x and y that
d = ax + by, which can be proven by assumption.

Then z must be multiples of d.
'''


class Solution(object):


    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(x, y):
            while x:
                x, y = y % x, x
            return y

        if x * y == 0:
            return z in (0, x, y)
        d = gcd(x, y)
        return z <= x + y and z % d == 0

def test():
    solution = Solution()

    assert solution.canMeasureWater(3, 5, 4)
    assert not solution.canMeasureWater(2, 6, 5)
    assert solution.canMeasureWater(2, 7, 9)
    assert solution.canMeasureWater(0, 0, 0)

    print('self test passed')

if __name__ == '__main__':
    test()
