#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
223. Rectangle Area

Total Accepted: 53819
Total Submissions: 169439
Difficulty: Easy
Contributors: Admin

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.


SOLUTION
================================================================================

Sum areas of individual rectangles, and subtract overlapping area.

How to get intersection of two rectangles?
This can be viewed in a line sweeping perspective.
To get the INTERSECTION border points, we just need to get the INNER MOST COORDINATE.


'''

class Solution(object):

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        x1 = max(A, E) # intersection bottom left
        y1 = max(B, F) # intersection bottom left
        x2 = min(C, G) # intersection top right
        y2 = min(D, H) # intersection top right
        # print('intersection:', (x1, y1), (x2, y2))
        # might be negative area if no intersection
        overlapped = (x2 - x1) * (y2 - y1) if x2 > x1 and y2 > y1 else 0
        area = (C - A) * (D - B) + (G - E) * (H - F) - overlapped
        return area

def test():
    solution = Solution()

    assert solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45
    assert solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2) == 16
    assert solution.computeArea(-2, -2, 2, 2, 3, 3, 4, 4) == 17

    print("self test passed")

if __name__ == '__main__':
    test()
