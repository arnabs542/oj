#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
436. Find Right Interval
Medium

Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

================================================================================
SOLUTION

1. Brute force

For each interval, enumerate and find the minimum index.

Complexity: O(N²)

2. Sort and binary search

Sort the indices array using key (interval start, index).

And use binary search to search lower bound.

Complexity: O(nlogn)


3. Binary search tree map
TODO: maybe use builtin bisect module.
This is language specific. For c++, is map. Use bst map to store <interval start, index>

"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

from _type import Interval

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        result = self._findRightIntervalSort(intervals)

        print(intervals, '=>', result)

        return result

    def _findRightIntervalSort(self, intervals):
        result = [-1 for _ in range(len(intervals))]

        indices = list(range(len(intervals)))
        # indices.sort(key=lambda x: (intervals[x].start, intervals[x].end, x)) # [2, 1, 0]
        indices.sort(key=lambda x: (intervals[x].start, x)) # [2, 1, 0]

        # print(indices)
        for i, j in enumerate(intervals):
            # result[j] = indices[i + 1] if i < len(intervals) - 1 else -1
            # binary search for lower bound?
            low, high = 0, len(indices) - 1
            while low <= high:
                mid = (low + high) // 2
                if intervals[indices[mid]].start >= intervals[i].end: high = mid - 1
                else: low = mid + 1
            result[i] = indices[low] if low < len(intervals) else -1
        return result # [-1, 0, 1]


def test():
    solution = Solution()

    assert solution.findRightInterval([]) == []
    assert solution.findRightInterval(list(map(lambda x: Interval(x[0], x[1]),
                                               [[1, 2]]
                                               ))) == [-1]
    assert solution.findRightInterval(
        list(map(lambda x: Interval(x[0], x[1]),
                 [ [3,4], [2,3], [1,2] ]))) == [-1, 0, 1]
    assert solution.findRightInterval(
        list(map(lambda x: Interval(x[0], x[1]),
                 [ [3,4], [1,2], [1,2] ]))) == [-1, 0, 0]
    assert solution.findRightInterval(
        list(map(lambda x: Interval(x[0], x[1]),
                 [ [1,2], [1,2], [1,2] ]))) == [-1, -1, -1]

    print ("self test passed!")

if __name__ == '__main__':
    test()
