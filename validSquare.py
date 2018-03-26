#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
593. Valid Square

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.

================================================================================
SOLUTION

1. Brute force
Exhaust all possible 4!=24 permutations, and verify the angle and length of each
side.

Complexity: O(24) = O(1)

2. Center point vector
Compute the center point, then we have exactly 4 vectors for a square.
Those four vectors must be of same vector length and collinear or perpendicular
to each other!

3. Points' distance have only two different values in integer grid square.
The given coordinates are all integers!

"""

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        result = self._validSquareCenterVector(p1, p2, p3, p4)

        print("result is: " ,result)

        return result

    def _validSquareCenterVector(self, p1, p2, p3, p4):
        minus = lambda x, y: (x[0] - y[0], x[1] - y[1])
        dot = lambda x, y: x[0] * y[0] + x[1] * y[1]

        center = [(p1[0] + p2[0] + p3[0] + p4[0])/4, (p1[1] + p2[1] + p3[1] + p4[1])/4]
        vectors = {minus(p1, center), minus(p2, center), minus(p3, center), minus(p4, center)}

        print(center, vectors)
        if len(vectors) < 4: return False
        a = None
        for v in vectors:
            if a is None:
                a = v
                continue
            product = dot(a, v)
            # same vector length and perpendicular or collinear
            if dot(v, v) != dot(a, a) or (product != 0 and product != -dot(a, a)):
                return False

        return True

    # TODO: sorting


def test():
    solution = Solution()

    assert not solution.validSquare([0, 0], [0, 0], [0, 0], [0, 0])
    assert solution.validSquare([0, 0], [1, 1], [1, 0], [0, 1])
    assert not solution.validSquare([0, 0], [1, 1], [1, 0], [0, 2])
    assert not solution.validSquare([1,1], [5,3], [3,5], [7,7])


    print("self test passed!")

if __name__ == '__main__':
    test()
