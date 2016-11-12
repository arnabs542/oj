#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
352. Data Stream as Disjoint Intervals

Total Accepted: 7627
Total Submissions: 19901
Difficulty: Hard
Contributors: Admin

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize
the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then
the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small
compared to the data stream's size?
===============================================================================================
SOLUTION:
    insert, and merge while it's possible.
'''

# Definition for an interval.
class Interval(object):

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ranges = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void

        Binary search solution

        339ms, 98.89%, 2016-10-29 15:59
        """
        low, high = 0, len(self.ranges) - 1
        # XXX: binary search
        while low <= high:
            mid = (low + high) >> 1
            if val < self.ranges[mid].start - 1:
                high = mid - 1
            elif val > self.ranges[mid].end + 1:
                low = mid + 1
            # break if val can be merged into Interval indexed at mid
            else:
                break

        if low <= high:
            # can merge
            if val == self.ranges[mid].start - 1:
                self.ranges[mid].start -= 1
                # merge leftwards or rightwards?
                while mid >= 1 and \
                      self.ranges[mid - 1].end + 1 >= self.ranges[mid].start:
                    self.ranges[mid].start = self.ranges[mid - 1].start
                    self.ranges.pop(mid - 1)
                    mid -= 1
            elif val == self.ranges[mid].end + 1:
                self.ranges[mid].end += 1
                while mid < len(self.ranges) - 1 and \
                      self.ranges[mid + 1].start - 1 <= self.ranges[mid].end:
                    self.ranges[mid].end = self.ranges[mid + 1].end
                    self.ranges.pop(mid + 1)
        else:
            # can't merge, just insert
            self.ranges.insert(max(low, high), Interval(val, val))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        print(self.ranges)
        return self.ranges

def test():
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)
    assert str(summaryRanges.getIntervals()) == '[[1, 1]]'
    summaryRanges.addNum(3)
    assert str(summaryRanges.getIntervals()) == '[[1, 1], [3, 3]]'
    summaryRanges.addNum(7)
    assert str(summaryRanges.getIntervals()) == '[[1, 1], [3, 3], [7, 7]]'
    summaryRanges.addNum(2)
    assert str(summaryRanges.getIntervals()) == '[[1, 3], [7, 7]]'
    summaryRanges.addNum(6)
    assert str(summaryRanges.getIntervals()) == '[[1, 3], [6, 7]]'

    summaryRanges.addNum(2)
    assert str(summaryRanges.getIntervals()) == '[[1, 3], [6, 7]]'

    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)
    assert str(summaryRanges.getIntervals()) == '[[1, 1]]'
    summaryRanges.addNum(5)
    summaryRanges.addNum(9)
    summaryRanges.addNum(6)
    summaryRanges.addNum(3)
    assert str(summaryRanges.getIntervals()) == '[[1, 1], [3, 3], [5, 6], [9, 9]]'

    print('self test passed')

if __name__ == '__main__':
    test()

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
