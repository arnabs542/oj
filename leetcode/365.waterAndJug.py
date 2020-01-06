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

- Fill any of the jugs completely with water.
- Empty any of the jugs.
- Pour water from one jug into another till the other jug is completely full or the first
jug itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

SOLUTION
================================================================================

1. Brute force - graph search - breadth first search

Define state:
graph vertex (p, q): volume of water in each jug respectively.

Initial state: (p=0, q=0).
State transition is via graph edges: operations allowed
    Fill: (x, p), (p, y)
    Empty: (0, q), (p, 0)
    Pour: (min(x, p+q), max(0, q-(x-p))), (max(0, p-(y-q)), min(y, p+q)),
Terminal state: z is in {p, q, p+q}.

Complexity:
We need to iterate all possible states that ax+by can represent.


2. Math - greatest common divisor
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
        # result = self.canMeasureWaterMath(x, y, z)
        result = self.canMeasureWaterBfs(x, y, z)

        print(x, y, z, result)
        return result

    def canMeasureWaterBfs(self, x, y, z):
        # special simple case
        if x + y < z: return False
        if x + y == z: return True
        if (x and z % x == 0) or (y and z % y) == 0: return True

        # bfs
        queue = [(0, 0)]
        visited = set({(0, ),})
        while queue:
            p, q = queue.pop()
            if z in (p, q, p + q): return True
            for p1, q1 in (
                (x, q), (p, y),
                (0, q), (p, 0),
                (min(x, p+q), max(0, q-(x-p))), (max(0, p-(y-q)), min(y, p+q)),
            ):
                if (p1, q1) in visited: continue
                queue.append((p1, q1))
                visited.add((p1, q1))

        return False

    def canMeasureWaterMath(self, x, y, z):

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

    assert solution.canMeasureWater(0, 0, 0)
    assert solution.canMeasureWater(3, 5, 4)
    assert not solution.canMeasureWater(2, 6, 5)
    assert solution.canMeasureWater(2, 7, 9)
    assert solution.canMeasureWater(3, 5, 6)
    assert solution.canMeasureWater(0, 0, 0)
    assert solution.canMeasureWater(6, 2, 4)
    assert not solution.canMeasureWater(104693, 104701, 324244)
    assert solution.canMeasureWater(1, 104701, 104700)


    print('self test passed')

if __name__ == '__main__':
    test()
