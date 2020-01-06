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
SOLUTION

This is a interval scheduling problem, illustrating greedy strategy property.

1. Sort and greedy remove
Sort the intervals according to their (start, end).

Scan the list from left to right, for two overlapping intervals, remove the proper one.

The problem is, which one to remove?
There might be an interval overlapping with every one, while others are nonoverlaping with
each other.
In this case, removing the one with larger end will do the trick.

Complexity: O(NlogN) + O(N²), worst case

2. Optimization of the above greedy strategy - Use a stack
Use a stack to pop from end of the list, and void inplace removing elements from a list.

Complexity: O(N) + O(NlogN) = O(NlogN)
Space complexity: O(N)

3. Optimization of the above greedy strategy
We don't have to output the intervals, we just need to count!

Complexity: O(N) + O(NlogN) = O(NlogN)
Space complexity: O(1)

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
        # result = self._eraseOverlapIntervalsGreedyNaive(intervals)
        result = self._eraseOverlapIntervalsGreedyOpt(intervals)

        return result

    def _eraseOverlapIntervalsGreedyNaive(self, intervals):
        # sort by key (start, end), or (start), or (end)
        # intervals.sort(key=lambda x: (x.start, x.end))
        intervals.sort(key=lambda x: x.start)
        n, i = 0, 1
        while i < len(intervals):
            if intervals[i].start < intervals[i - 1].end:
                j = i if intervals[i].end >= intervals[i - 1].end else i - 1
                intervals.pop(j) # list.pop complexity is O(N), don't use this
                n += 1
            else:
                i += 1

        return n

    def _eraseOverlapIntervalsGreedyOpt(self, intervals):
        # if len(intervals) <= 1: return len(intervals)

        intervals.sort(key=lambda x: (x.start, x.end))
        end = float('-inf')
        count = 0
        for interval in intervals:
            if interval.start >= end:
                count += 1
                end = interval.end # append a new interval
            else:
                end = min(end, interval.end) # replace
        return len(intervals) - count

    # TODO: output the non-overlapping intervals
    # implement with stack will achieve O(N), because it supports O(1) remove at the end.

def test():
    solution = Solution()

    assert solution.eraseOverlapIntervals(
        list(map(lambda x: Interval(x[0], x[1]),
                 []
                 ))) == 0
    assert solution.eraseOverlapIntervals(
        list(map(lambda x: Interval(x[0], x[1]),
                 [[1, 3], [2, 3], [3, 4], [1, 3]]
                 ))) == 2
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

    assert solution.eraseOverlapIntervals(
        list(map(lambda x: Interval(x[0], x[1]),
                 [[2, 9], [1, 3], [2, 4]]
                 ))) == 2

    print('self test passed')

test()
