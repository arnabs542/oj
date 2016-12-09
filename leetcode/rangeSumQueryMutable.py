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

SOLUTION:
    1. Segment tree
    2. Binary indexed tree
'''

import math

# TODO: representation of segment tree to make the interface simpler
class SegmentTree(object):

    def __init__(self, nums):
        self.nums = nums
        if not nums:
            self.height = 0
        else:
            self.height = math.ceil(math.log(len(nums), 2))
            # full binary tree, using array representation
            self.tree = [0] * int(pow(2, self.height + 1) - 1)
            self.construct(0, 0, len(nums) - 1)
        pass

    def construct(self, idx: int, left: int, right: int):
        '''
        idx: tree node index in array representation
        left, right: segment range
        '''
        if left == right:
            self.tree[idx] = self.nums[left]
        else:
            mid = (left + right) >> 1
            self.tree[idx] = self.construct(2 * idx + 1, left, mid) + \
                self.construct(2 * idx + 2, mid + 1, right)
        return self.tree[idx]

    def update(self, i, val):
        '''
        update element at index i to value val
        '''
        if not 0 <= i <= len(self.nums) - 1:
            return
        diff = val - self.nums[i]
        self.nums[i] = val
        self.updateUtil(
            i, diff, 0, left=0, right=len(self.nums) - 1)

    def updateUtil(self, i, diff, idx, left, right):
        '''
        idx: tree node index in array representation
        left, right: segment range

        Add difference to update instead of pure set operation.
        '''
        if left <= i <= right:
            self.tree[idx] += diff
            mid = (left + right) >> 1
            if left < right:
                self.updateUtil(i, diff, 2 * idx + 1, left, mid)
                self.updateUtil(i, diff, 2 * idx + 2, mid + 1, right)
        pass

    def query(self, i, j, idx=0, left=0, right=-1):
        '''
        idx: tree node index in array representation
        left, right: segment range
        '''
        if not idx:
            left, right = 0, len(self.nums) - 1
        if not 0 <= i <= j <= len(self.nums) - 1:
            # invalid query
            return 0
        if (i > j) or j < left or i > right:
            # out of range
            return 0
        elif i <= left and right <= j: # return the full range
            return self.tree[idx]
        else:
            mid = (left + right) >> 1
            return self.query(i, j, 2 * idx + 1, left=left, right=mid) + \
                self.query(i, j, 2 * idx + 2, left=mid + 1, right=right)

class BinaryIndexedTree(object):
    # TODO: binary indexed tree

    def __init__(self, nums):
        pass

    def update(self):
        pass

    def query(self):
        pass

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
