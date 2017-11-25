#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
56. Merge Intervals

Total Accepted: 86690
Total Submissions: 316815
Difficulty: Hard
Contributors: Admin

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)

class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        # intervals = self.mergeTrivial(intervals)
        intervals = self.mergeStack(intervals)
        print(intervals)
        return intervals

    def mergeTrivial(self, intervals):
        i = 0
        while i < len(intervals) - 1:
            if intervals[i].end >= intervals[i + 1].start:
                # merge
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end)
                intervals.pop(i + 1)
            else:
                i += 1

    def mergeStack(self, intervals):
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
                continue
            intervalPre = stack.pop()
            if intervalPre.end >= interval.start:
                intervalNew = Interval(intervalPre.start, max(intervalPre.end, interval.end))
                stack.append(intervalNew)
            else:
                stack.append(intervalPre)
                stack.append(interval)

        return stack

def test():
    solution = Solution()
    assert list(map(lambda x: [x.start, x.end], (solution.merge(list(map(
        lambda x: Interval(x[0], x[1]), [[1, 3], [2, 6], [8, 10], [15, 18]])))))) == [[1, 6], [8, 10], [15, 18]]
    assert list(map(lambda x: [x.start, x.end], (solution.merge(list(map(
        lambda x: Interval(x[0], x[1]), [[1, 4], [2, 3]])))))) == [[1, 4]]
    pass

if __name__ == '__main__':
    test()
