#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
57. Insert Interval

Total Accepted: 72678
Total Submissions: 284450
Difficulty: Hard
Contributors: Admin

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if
necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

==============================================================================================
SOLUTION

1. Sort and insert
Sort the original intervals list, and iterate over the original list. Then the process is like
merge sort.

Complexity: O(NlogN) + O(N)

'''

# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

class Solution(object):

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        merged_intervals = []
        i = 0
        for interval in intervals:
            if not newInterval:
                merged_intervals.append(interval)
                continue
            if interval.end < newInterval.start:
                merged_intervals.append(interval)
            elif interval.start > newInterval.end:
                merged_intervals.append(newInterval)
                merged_intervals.append(interval)
                newInterval = None
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
            pass

        if newInterval:
            merged_intervals.append(newInterval)

        print(merged_intervals)
        return merged_intervals

def test():
    solution = Solution()
    assert solution.insert(
        list(map(lambda x: Interval(x[0], x[1]), [[1, 3], [6, 9]])), Interval(2, 5)) == \
        list(map(lambda x: Interval(x[0], x[1]), [[1, 5], [6, 9]]))
    print('self test passed')

if __name__ == '__main__':
    test()
