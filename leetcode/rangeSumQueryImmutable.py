#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j),
inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.


==============================================================================================
SOLUTION

Sparse table can be used for range minimum query. Can it be modified to do the job?

1. Brute force

Complexity: O(N)

2. Cache
Build a table t, where t[i][j] indicates the sum between i and j.


Complexity: O(N²) initialization, O(1) for query

3. Prefix sum

Sum between can be computed by differentiating: calculate the cumulative/prefix sum(integral)
and take the difference of two ends.

Complexity: build O(n), query O(1)

4. Segment tree
Complexity: build O(nlogn), query O(1)

5. Binary indexed tree?

'''

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.prefixSum = [0]
        for i, num in enumerate(nums):
            self.prefixSum.append(self.prefixSum[-1] + num)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if not 0 <= i <= j < len(self.nums):
            print("illegal input!")
            return None
        return self.prefixSum[j + 1] - self.prefixSum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

def test():
    obj = NumArray([-2, 0, 3, -5, 2, -1])

    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
    assert obj.sumRange(3, 3) == -5
    assert obj.sumRange(0, 5) == -3

    print("self test passed")

if __name__ == '__main__':
    test()
