#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
452. Minimum Number of Arrows to Burst Balloons

Total Accepted: 2232
Total Submissions: 5286
Difficulty: Medium
Contributors: abhijeeg

There are a number of spherical balloons spread in two-dimensional space. For each balloon,
provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal,
y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice.
Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon
with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to
the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The
problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and
another arrow at x = 11 (bursting the other two balloons).
==============================================================================================
SOLUTION:
    Just merge intervals into intersection where possible, the final number of intervals is the
solution.
'''

class Solution(object):

    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x: x[0])
        i = 1
        while i < len(points):
            if points[i][0] <= points[i - 1][1]:
                points[i][1] = min(points[i - 1][1], points[i][1])
                # print('merged', points[i])
                points.pop(i - 1)
            else:
                i += 1

        print(points)
        return len(points)

    def findMinArrowShotsOpt(self, points):
        """
        :type points: List[List[int]]
        :rtype: int

        Only count non-overlapping intervals, instead of manipulating them
        """
        points = sorted(points, key=lambda x: x[1])
        res, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:
                res += 1
                end = interval[1]
        return res

def test():
    solution = Solution()

    assert solution.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert solution.findMinArrowShots([[1, 2], [2, 3]]) == 1
    assert solution.findMinArrowShots([[1, 2], [2, 3], [3, 4]]) == 2

    assert solution.findMinArrowShots(
        [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]) == 2

    assert solution.findMinArrowShots([]) == 0

    assert solution.findMinArrowShots(
        [[1, 3], [2, 6], [8, 10], [15, 18]]) == 3
    assert solution.findMinArrowShots(
        [[1, 4], [2, 3]]) == len([[1, 4]])

    print('self test passed')
    pass

if __name__ == '__main__':
    test()
