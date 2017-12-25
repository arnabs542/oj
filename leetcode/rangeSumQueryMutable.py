#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
307. Range Sum Query - Mutable

Total Accepted: 21089
Total Submissions: 113775
Difficulty: Medium
Contributors: Admin

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j),
inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

==============================================================================================
SOLUTION
1. Segment tree
2. Binary indexed tree

'''

from _tree import SegmentTree

class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.segmentTree = SegmentTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.segmentTree.update(i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        result = self.segmentTree.query(i, j, 0)
        print('[{i}, {j}]: {result}'.format(i=i, j=j, result=result))
        return result


def test():
    # Your NumArray object will be instantiated and called as such:
    nums = []
    numArray = NumArray(nums)
    assert numArray.sumRange(0, 2) == 0

    nums = [-1]
    numArray = NumArray(nums)
    assert numArray.sumRange(0, 0) == -1
    numArray.update(0, 1)
    numArray.sumRange(0, 0)

    nums = [1, 3, 5, 7, 9, 11]
    numArray = NumArray(nums)
    assert numArray.sumRange(1, 3) == 15
    numArray.update(1, 10)
    assert numArray.sumRange(1, 3) == 22

    nums = [1, 3, 5]
    numArray = NumArray(nums)
    assert numArray.sumRange(0, 2) == 9
    numArray.update(1, 2)
    assert numArray.sumRange(0, 2) == 8

    nums = [7, 2, 7, 2, 0]
    numArray = NumArray(nums)
    numArray.update(4, 6)
    numArray.update(0, 2)
    numArray.update(0, 9)
    assert numArray.sumRange(4, 4) == 6
    numArray.update(3, 8)
    assert numArray.sumRange(0, 4) == 32

if __name__ == '__main__':
    test()
