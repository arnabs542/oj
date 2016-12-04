#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
11. Container With Most Water

Total Accepted: 105888
Total Submissions: 294449
Difficulty: Medium
Contributors: Admin

Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is
at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container.

==============================================================================================
SOLUTION:
    1. A brute-force solution would be compute all pair-wise container volume, time complexity
O(N*N) = O(N^2).

    2. Two pointers Harnessing the (short plate theory)bucket effect:
the SHORT PLATE is the limiting factor of VOLUME of a bucket rather than the longer ones.

Illustrating in a matrix representation:

Draw a matrix where the row is the first line, and the column is the second line. For example,
say n=6.

In the figures below, x means we don't need to compute the volume for that case: (1) On the
diagonal, the two lines are overlapped; (2) The lower left triangle area of the matrix is
symmetric to the upper right area.

We start by computing the volume at (1,6), denoted by 'o'. Now if the left line is shorter
than the right line, then all the elements left to (1,6) on the first row have smaller volume,
so we don't need to compute those cases (crossed by ---).

  1 2 3 4 5 6
1 x ------- o
2 x x
3 x x x
4 x x x x
5 x x x x x
6 x x x x x x

Next we move the left line and compute (2,6). Now if the right line is shorter, all cases
below (2,6) are eliminated.

  1 2 3 4 5 6
1 x ------- o
2 x x       o
3 x x x     |
4 x x x x   |
5 x x x x x |
6 x x x x x x
And no matter how this o path goes, we end up only need to find the max value on this path,
which contains n-1 cases.

  1 2 3 4 5 6
1 x ------- o
2 x x - o o o
3 x x x o | |
4 x x x x | |
5 x x x x x |
6 x x x x x x
'''

class Solution(object):

    def maxArea(self, height) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        max_volume = 0
        while i < j:
            width = j - i
            if height[i] < height[j]:
                volume = height[i] * width
                i = i + 1
            else:
                volume = height[j] * width
                j = j - 1

            max_volume = max(volume, max_volume)

        return max_volume

def test():
    solution = Solution()

    assert solution.maxArea([1, 1]) == 1

    print('self test passed')

if __name__ == '__main__':
    test()
