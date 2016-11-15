#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
435. Non-overlapping Intervals

Total Accepted: 1922
Total Submissions: 4971
Difficulty: Medium
Contributors: love_FDU_llp

Given a collection of intervals, find the minimum number of intervals you need to
remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
==============================================================================================
SOLUTION:
    1) sort the intervals according to their (start, end). Scan the list from left to right, once
we find two overlapping intervals, remove the one with larger range.
'''

# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):

    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        # sort by key (start, end), or (start), or (end)
        # intervals.sort(key=lambda x: (x.start, x.end))
        intervals.sort(key=lambda x: x.start)
        n, i = 0, 1
        while i < len(intervals):
            if intervals[i].start < intervals[i - 1].end:
                j = i if intervals[i].end >= intervals[i - 1].end else i - 1
                intervals.pop(j)
                n += 1
            else:
                i += 1

        return n

def test():
    solution = Solution()

    assert solution.eraseOverlapIntervals(
        list(map(lambda x: Interval(x[0], x[1]),
                 [[1, 2], [2, 3], [3, 4], [1, 3]]
                 ))) == 1
    assert solution.eraseOverlapIntervals(
        list(map(lambda x: Interval(x[0], x[1]),
                 [[1, 2], [1, 2], [1, 2]]
                 ))) == 2
    assert solution.eraseOverlapIntervals(
        list(map(lambda x: Interval(x[0], x[1]),
                 [[-1, 9], [1, 3], [2, 4]]
                 ))) == 2
    assert solution.eraseOverlapIntervals(
        list(map(lambda x: Interval(x[0], x[1]),
                 [[2, 9], [1, 3], [2, 4]]
                 ))) == 2

    print('self test passed')

test()
