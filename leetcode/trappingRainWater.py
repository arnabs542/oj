#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
42. Trapping Rain Water

Total Accepted: 89795
Total Submissions: 257814
Difficulty: Hard
Contributors: Admin

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this
case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for
contributing this image!

==============================================================================================
SOLUTION:
    A interval container's height is determined by the short slab.
    By analysis, we can see the key points are the increasing subsequence's end.

Array:                    [0, 1, 0, 2, 1, 0, 1, 3, 2,  1, 2, 1]
Difference(derivatives) : [0, 1,-1, 2,-1, 0, 1, 2,-1, -1, 1,-1]
Increasing ends:  [1, 3, 7, 10] (with positive derivatives)

1. Find local maxima with FIRST-ORDER DERIVATIVES or some linear scanning algorithm.
2. Remove local minima of local maxima.
3. Compute the AREA UNDER CURVE between two points.

The interval between two consecutive local maximum points are valid container for trapping
water.

'''

class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        return self.trapDerivative(height)

    def trapDerivative(self, height: list) -> int:
        """
        :type height: List[int]
        :rtype: int

        Use first-order derivatives to find local maxima and local minima of them.
        """
        derivatives = list(map(
            lambda x: height[x[0]] - height[x[0] - 1] if x[0] else x[1],
            enumerate(height)
        ))
        ends = []
        # find local maxima
        for i in range(1, len(derivatives) + 1):
            if (i == len(derivatives) or derivatives[i] <= 0) and derivatives[i - 1] > 0:
                ends.append((i - 1, height[i - 1]))

        # remove local minimum
        i = 1
        print(ends)
        while 0 < i < len(ends) - 1:
            if ends[i - 1][1] >= ends[i][1] <= ends[i + 1][1]:
                ends.pop(i)
                if i >= 2: i -= 1
            else:
                i += 1
        print(ends)

        # compute area under curve between two points
        amount = 0
        for i in range(len(ends) - 1):
            shortSlab = min(height[ends[i][0]], height[ends[i + 1][0]])
            for j in range(ends[i][0] + 1, ends[i + 1][0]):
                amount += max(shortSlab - height[j], 0)

        print(amount)
        return amount

    def trapTwoPointers(self, height: list) -> int:
        '''
        Two pointers algorithm.
        '''
        return 0


def test():
    solution = Solution()

    assert solution.trap([]) == 0
    assert solution.trap([5, 4, 1, 2]) == 1
    assert solution.trap([5, 2, 1, 2, 1, 5]) == 14
    assert solution.trap([1, 2, 3, 0, 4]) == 3
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solution.trap([1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solution.trap([8, 8, 1, 5, 6, 2, 5, 3, 3, 9]) == 31
    assert solution.trap([6, 0, 3, 0, 3, 1, 5]) == 18
    assert solution.trap([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5,
                          3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]) == 83
    print('self test passed')

if __name__ == '__main__':
    test()
