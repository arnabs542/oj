#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
84. Largest Rectangle in Histogram

Total Accepted: 76666
Total Submissions: 300455
Difficulty: Hard
Contributors: Admin

Given n non-negative integers representing the histogram's bar height where the width
of each bar is 1, find the area of largest rectangle in the histogram.

[img](./largest_rectangle_in_histogram_i.png)

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

[img](./largest_rectangle_in_histogram_ii.png)

The largest rectangle is shown in the shaded area(5, 6), which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

================================================================================
SOLUTION:

1. Brute-force.
Find all pairs in O(N²), and compute area in O(1),

f(i, j) = min(height[i, ..., j]) * (j - i + 1),  1 <= i, j <=  n
And we want to get max(f(i, j)).

i, j pairs are of O(N²) complexity, since it involves two loops.
(j - i + 1) is O(1) time complexity, and get query the range minimum is of O(0) because
we can keep track of that while iterating with j index in the inner loop.

Or in a bar PERSPECTIVE, exhaust all bars. For each bar, choose it as height of
rectangle. Find the longest window containing it and with elements no smaller than it.
Then area = height[i] * window size.


Complexity: O(N²).


The rectangle must have a smallest bar, and that's the height of this rectangle.
--------------------------------------------------------------------------------

2. Divide and conquer

The above solution involves duplicate computations.

When computing area of a rectangle formed by a group of bars, the height is decided by the
bar with minimal height. This can form a greedy strategy to eliminate some duplicate cases.

There exists a minimum height in the histogram.

And there is a greedy strategy:
If incorporating the minimum bar into the rectangle, there is no need to compute all possible
rectangles, because among those rectangles including this minimal height bar, the one
starting and ending with two ends of the histogram will have the maximum area.

----------------------------------------------------------------------------------------------
Find the minimum, divide the problem into two parts.


The max area is maximum of three scenarios:
a) Maximum area in left side of minimum height bar (exclusive)
b) Maximum area in right side of minimum height bar (inclusive)
c) Maximum area obtained by number of bars multiplied by minimum height.

But if we use naive divide and conquer, the worst case time complexity could be O(N²).
Complexity
T(n) = 2T(n/2) + O(n), so average time complexity is O(NlogN).
Worst case is O(N²).

3. Divide and conquer optimized

Duplicate calculations of range minimum query, when computing area bounded by a pair of bars.
Linear scanning for range minimum query is O(n) complexity.

Can we optimize the range minimum query process?
Preprocessing the array to build segment tree, sparse table, binary indexed tree?

If we build a range minimum query data structure, of course not look up table with O(N²), with
a tree data structure. Then rmq takes O(logN).

But, unfortunately, the average time complexity isn't reduced.
Because the tree is built only once, every subproblem takes same time complexity to do
range minimum query, O(logN), regardless of the smaller size of subproblem.
The complexity is still O(nlogn) on average.

However, THE WORST CASE COMPLEXITY IS REDUCED to O(nlogn)!

Complexity: O(nlogn) for both average and worst case!

For large data set with length 20000, the speed up can be 1400 times in worst case in theory!
15033.65/

4. Monotonicity analysis - monotone stack

In a brute force method, for each bar x, compute the area with x as height.
Then we need to know the INDEX OF FIRST SMALLER bar on left and right of x.

The simplest case is when the array in monotonically increasing or decreasing.

1) What if it's increasing?
Then all possible largest rectangle would literally end with the largest bar.
Like in [1, 2, 3, 4], previous position of each bar is the index of first smaller
on the left.
Areas candidates:
1*4 = 4
2*3 = 6
3*2 = 6
4*1 = 1,
for each index i, it is area = a[i] * (n-i).
This means, we can't determine the largest rectangle with height a[i] until the
last one. So we have to process BACKWARD.

Processing BACKWARD means using a STACK, and accumulate results when popping!
--------------------------------------------------------------------------------

2) What if it's decreasing?
Then each bar can form a potentially largest rectangle starting with the first bar.

3) What if we have a increasing sequence, then a lower value comes?
For the stack top element, the indices of first smaller element on left and right
are all determined!
Then we have all information needed to compute the rectangle with this bar height.

--------------------------------------------------------------------------------
Maintain a monotonically increasing stack.

- Push for increasing subsequence.
- Pop until stack empty of stack top is smaller than current element.
Remember: The bottom element of the stack means every element before it is larger
than it!
When popping i, calculate largest rectangle area with height a[i].

For the stack top, the current bar that's smaller than it is the first index of smaller
bar on right. And the second top element in the stack is the first smaller index on left.
The area of rectangle with stack top bar height is given by:
    area = width * height(stack top),
where width is determined by the gap between second top element of the stack and
current element.


  2 1 5 6 2 3
2 2
1
5
6
2
3

Complexity: O(n), O(n)

5. Dynamic programming
Keep track of three variables as state:
    current bar height, left boundary, right boundary.

TODO: figure it out...

'''

from _tree import SegmentTree
from _decorators import timeit

class Solution(object):

    @timeit
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # result = self._largestRectangleAreaRMQ(heights)
        # result = self._largestRectangleAreaDivideAndConquer(heights)
        # result = self._largestRectangleAreaDivideAndConquerIterative(heights)
        # result = self._largestRectangleAreaDivideAndConquerRMQ(heights)
        result = self._largestRectangleAreaMonotoneStack(heights)

        print(heights[:100], ", result: ", result)
        return result

    def _largestRectangleAreaDivideAndConquer(self, heights: list) -> int:
        # FIXME: recursive implementation exceeds maximum recursion depth...
        def dfs(left, right):
            # print(left, right)
            if left > right:
                return 0
            iMin, hMin = 0, float('inf')
            for i in range(left, right+1):
                if heights[i] < hMin:
                    iMin = i # 1
                    hMin = heights[i] # 1
            area = max(hMin * (right - left + 1), dfs(left, iMin - 1), dfs(iMin + 1, right)) # max(6, 2, max(8, 10, 3))
            return area

        area = dfs(0, len(heights) - 1) # 0, 5
        return area

    def _largestRectangleAreaDivideAndConquerIterative(self, heights: list) -> int:
        # FIXME: still O(N²), in worst case.
        area = 0
        stack = [(0, len(heights) - 1)]

        while stack:
            left, right = stack.pop()
            # print(left, right)
            if left > right: continue
            iMin, hMin = 0, float('inf')
            for i in range(left, right+1):
                if heights[i] < hMin:
                    iMin = i # 1
                    hMin = heights[i] # 1
            area = max(area, hMin * (right - left + 1))

            stack.append((left, iMin - 1))
            stack.append((iMin + 1, right))

        # area = dfs(0, len(heights) - 1) # 0, 5
        return area

    def _largestRectangleAreaDivideAndConquerRMQ(self, heights: list) -> int:
        """
        Divide and conquer optimized with efficient range minimum query to reduce worst case complexity
        Comlexity: O(nlogn)

        Runtime: 1516 ms
        """
        # DONE: build range minimum query data structure
        tree = SegmentTree(heights, 'rmq')

        area = 0
        stack = [(0, len(heights) - 1)]
        while stack:
            left, right = stack.pop()
            if left > right: continue
            # DONE: efficient range minimum query
            iMin = tree.query(left, right, index=True)
            hMin = heights[iMin]
            area = max(area, hMin * (right - left + 1))

            stack.append((left, iMin - 1))
            stack.append((iMin + 1, right))

        return area

    def _largestRectangleAreaMonotoneStack(self, heights: list) -> int:
        area = 0

        stack = []
        heights.append(-1) # add a sentinel
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                j = stack.pop()
                left = stack[-1] + 1 if stack else 0
                width = i - left
                area = max(area, width * heights[j])

            stack.append(i)

        return area

def test():
    solution = Solution()

    assert solution.largestRectangleArea([]) == 0
    assert solution.largestRectangleArea([0]) == 0
    assert solution.largestRectangleArea([1]) == 1
    assert solution.largestRectangleArea([0, 1]) == 1
    assert solution.largestRectangleArea([1, 1]) == 2
    assert solution.largestRectangleArea([1, 1]) == 2
    assert solution.largestRectangleArea([1, 1, 1]) == 3
    assert solution.largestRectangleArea([2, 1, 2]) == 3
    assert solution.largestRectangleArea([4, 2, 0, 3, 2, 5]) == 6
    assert solution.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert solution.largestRectangleArea([1, 2, 3, 4, 5, 6]) == 12

    # large data test
    import yaml
    data = []
    with open("./largestRectangleInHistogram.json", "r") as f:
        data = yaml.load(f)
    for record in data:
        assert solution.largestRectangleArea(record['input']) == record['output']

    print("large data set passed!")

    print('self test passed')

if __name__ == '__main__':

    test()
