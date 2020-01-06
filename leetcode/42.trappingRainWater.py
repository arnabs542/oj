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


================================================================================
SOLUTION

By observing the physical process, a container is determined by two side bars.
Valid containers have side bars formed by local maxima.
A container's valid height is determined by the short slab of two sides.

1. Brute force
Exhaust all bars, accumulate volume of water above the bars.
For each bar, the container two sides must be, maximum on the left and right.

For each bar, scan all bars on the left and on the right, searching for
maximum value. And compute, accumulate the water volume above each bar.

Complexity: O(NN) = O(N²), O(1)

2. Dynamic programming - efficient range query for maximum so far

Use auxiliary space to store maximum so far on left and right to enable O(1)
range query maximum.

Scan from left to right to store maximum from subarray [0,...,i] in left[i].
Scan from right to left to store maximum from subarray [i,...,n] in right[i].

Then, for each bar in the height array, we can find the valid container height
on both sides in O(1).

Complexity: O(n), O(n)

3. Monotonicity and extrema points analysis naive - container contour perspective
Accumulate volume of all valid containers.

This is a two passes solution.
First, exhaust all valid containers contours, then compute are between containers.

By analysis of the MONOTONICITY property, we can see the key points are the increasing
subsequence's local EXTREMA, i.e., the LOCAL MAXIMUM.

Find all local maxima, and remove the strictly local minimum of those local maxima

Array:                    [0, 1, 0, 2, 1, 0, 1, 3, 2,  1, 2, 1]
Difference(derivatives) : [0, 1,-1, 2,-1, 0, 1, 2,-1, -1, 1,-1]
Increasing maximum bars:  [1, 3, 7, 10] (with positive derivatives)

1) Find local maxima with FIRST-ORDER DERIVATIVES or some linear scanning algorithm.
2) Recursively remove local minima of previously found local maxima. So that we
will only have at most one increasing and one decreasing major bins sequence,
i.e., a peak shape sequence.
3) Compute the AREA UNDER CURVE between two points.

The interval between two consecutive local maximum points are valid container for trapping
water.

If the recursive deleting elements isn't implemented correctly, for example,
deleting from array inplace, the complexity would go to O(N²). Since removing
from a list is O(N).

Complexity: O(N²), O(N)

4. Two MONOTONIC STACK - Extrema points analysis - container contour perspective
Still, exhaust all valid containers contours, accumulate volume of all valid containers.

A container must have two outside bounds! What will that be?
Apparently, the container must have local maxima as outmost bounds.

Then, find maxima points. Just remember to rule out those local minima of local maxima.

The local maxima set must form a increasing, then decreasing trend. There must be
not local minima of the local maxima, otherwise this bar isn't a valid side of
the water container.

--------------------------------------------------------------------------------
Use two stacks to maintain monotonic local maxima.
1) One increasing stack to keep non-decreasing values.
2) One decreasing stack to keep non-increasing values.
For each new element, maintain the stacks using state transition:
    1) pop out smaller elements in stack 2.
    2) if stack2 is empty and new element is larger than stack 1 top element, then
push new element into stack1
    2) else, push it into the stack 2

Finally, concatenate two stacks into one array,

Complexity: O(N), O(N).

5. One MONOTONIC Stack - bar perspective
Instead of trying to find the container contours, accumulate water
rectangle volume above each bar horizon level!

Maintain a monotonic decreasing stack. Scan the list from left to right.
If a new element is larger than stack top bar, it means it will form a partial
container. Though it may not be the ultimate container, we can keep adding
volume level by level.

Complexity: O(N), O(N)

6. Two pointers - two ends to middle
Compute the are in a cumulative way with two pointers, from both sides to middle.

Observation: if a container composed of two bins can't hold that much water, then there will
be overflow. And water will flow from inside the container to outside. And the outside most
container is deterministic: the boundary!

So we could start with two pointers from two ends to meet at middle.

Search from left to right and maintain a max height of left and right separately, which
act like an actually valid outside container's walls to prevent overflow.

Fix the higher one and flow water to the lower barrier. For example, if current height
of left is lower, we fill water in the left bin. Until left meets right, we fill the
whole container.

Complexity: O(n), O(1)

'''

class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # result = self._trapExtremaPointsNaive(height)
        # result = self._trapExtremaPointsStack(height)
        # result = self._trapOneStack(height)
        result = self._trapTwoPointers(height)

        print(height, result)

        return result

    def _trapExtremaPointsNaive(self, height: list) -> int:
        """
        :type height: List[int]
        :rtype: int

        Use first-order derivatives to find local maxima and local minima of them.

        Deleting local minima from array by calling  pop(i) is O(N).

        Complexity: O(N²) in worst case

        TODO: improve it
        """
        derivatives = list(map(
            lambda x: height[x[0]] - height[x[0] - 1] if x[0] else x[1],
            enumerate(height)
        ))
        maxima = []
        # find local maxima
        for i in range(1, len(derivatives) + 1):
            if (i == len(derivatives) or derivatives[i] <= 0) and derivatives[i - 1] > 0:
                maxima.append((i - 1, height[i - 1]))

        # remove local minimum of maxima
        i = 1
        print(maxima)
        while 0 < i < len(maxima) - 1:
            if maxima[i - 1][1] >= maxima[i][1] <= maxima[i + 1][1]:
                maxima.pop(i)
                if i >= 2: i -= 1
            else:
                i += 1
        print(maxima)

        # compute area under curve between two points
        amount = 0
        for i in range(len(maxima) - 1):
            shortSlab = min(height[maxima[i][0]], height[maxima[i + 1][0]])
            for j in range(maxima[i][0] + 1, maxima[i + 1][0]):
                amount += max(shortSlab - height[j], 0)

        print(amount)
        return amount

    # DONE: more efficient deleting local minima
    def _trapExtremaPointsStack(self, height: list) -> int:
        """
        Find monotonic local maxima with two stacks.

        Maintain a increasing stack, for increasing local maxima.
        Maintain a decreasing stack, for decreasing local maxima.

        For a new element, from the decreasing stack, popping smaller one out.
        And if, the new element is even larger than increasing stack top,
        then push it into the increasing stack. Else, push it into the decresing
        stack.

        """
        # build two monotonic stacks: forming a peak shape
        ascend = [] # 5, 5
        descend = [] #
        for i, h in enumerate(height):
            while descend and height[descend[-1]] < h:
                descend.pop() # keep equal ones
            if not descend and (not ascend or height[ascend[-1]] <= h):
                ascend.append(i)
            else:
                descend.append(i)
            pass

        maxima = ascend + descend
        area = 0

        # print("local maxima: ", maxima)
        # compute rectangle area between successive local maxima
        for i in range(len(maxima) - 1):
            left, right = maxima[i], maxima[i + 1]
            h = min(height[left], height[right])
            for j in range(left + 1, right):
                area += max(h - height[j], 0)
        return area

    def _trapOneStack(self, height: list) -> int:
        stack = []
        area = 0
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                bottom = stack.pop()
                if not stack: break
                left = stack[-1]
                width = i - left - 1
                boundedHeight = min(h, height[left]) - height[bottom]
                area += width * boundedHeight # horizontal rectangle
            stack.append(i)

        return area

    def _trapTwoPointers(self, height: list) -> int:
        '''
        Two pointers algorithm.
        '''
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        area = 0
        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                area += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                area += right_max - height[right]
                right -= 1
                pass
            pass
        return area


def test():
    solution = Solution()

    assert solution.trap([]) == 0
    assert solution.trap([5, 4, 1, 2]) == 1
    assert solution.trap([5, 1, 3, 6]) == 6
    assert solution.trap([1, 2, 3, 0, 4]) == 3
    assert solution.trap([5, 2, 1, 2, 1, 5]) == 14
    assert solution.trap([6, 0, 3, 0, 3, 1, 5]) == 18
    assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solution.trap([1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert solution.trap([8, 8, 1, 5, 6, 2, 5, 3, 3, 9]) == 31
    assert solution.trap([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5,
                          3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]) == 83
    print('self test passed')

if __name__ == '__main__':
    test()
