#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
469. Convex Polygon

Given a list of points that form a polygon when joined sequentially, find if this
polygon is convex.

Note:
    1. There are at least 3 and at most 10,000 points.
    2. Coordinates are in the range -10,000 to 10,000.
    3. You may assume the polygon formed by given points is always a simple polygon.
    In other words, we ensure that exactly two edges intersect each vertex, and that edges
otherwise don't intersect each other.

==============================================================================================
SOLUTION

Observation: Convexity is equivalent to whether the adjacent edge vectors always turn to the
same direction, clockwise or counter clockwise, i.e., cross product (pᵢ+₁-pᵢ) x (pᵢ+₂-pᵢ)
does not change sign when traversing sequentially along polygon vertices.

And cross product can be computed in a matrix determinant way.

Refer to https://en.wikipedia.org/wiki/Cross_product for cross product.

'''

class Solution(object):

    def isConvex(self, points: list):

        def _det2(u, v):
            '''
            compute the cross product
            '''
            return (u[1] * v[2] - u[2] * v[1],
                    u[0] * u[2] - u[2] * v[0],
                    u[0] * v[1] - u[1] * v[0])

        prev, curr = 0, 0 # the previous and current direction
        n = len(points)
        for i, _ in enumerate(points):
            u = (points[i][0] - points[i - 1][0], points[i][1] - points[i - 1][1], 0)
            v = (points[(i + 1) % n][0] - points[i][0], points[(i + 1) % n][1] - points[i][1], 0)
            curr = _det2(u, v)[2]
            if curr * prev < 0:
                return False
            prev = curr
        return True


def test():
    solution = Solution()

    assert solution.isConvex([[0, 0], [0, 1], [1, 1], [1, 0]])
    assert not solution.isConvex([[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]])

    print("self test passed")

if __name__ == '__main__':
    test()
