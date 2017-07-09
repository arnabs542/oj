#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice
and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

==============================================================================================
SOLUTION


----------------------------------------------------------------------------------------------
Reference

Similar to firstMissingPositive.py.


1. 1 Pass ?

2. 2 Passes
    1) Put those values in right buckets
    2) Check those that can't fit into the right bucket, and they are duplicates

'''

class Solution(object):

    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = self._findDuplicatesBucketOnePass(nums)
        result = self._findDuplicatesBucketTwoPasses(nums)
        print(nums, result)
        return result

    def _findDuplicatesBucketOnePass(self, nums):
        # TODO: one pass solution?
        result = []
        i = 0
        while i < len(nums):
            n = nums[i]
            if nums[n - 1] == n: # value already put in right position
                if n - 1 < i: # but not current position
                    # print('found duplicate')
                    result.append(n)
                i += 1
            else:
                nums[n - 1], nums[i] = n, nums[n - 1]
        return result

    def _findDuplicatesBucketTwoPasses(self, nums):
        result = []
        i = 0
        while i < len(nums):
            n = nums[i]
            if nums[n - 1] == n: # value already put in right position
                i += 1
            else: nums[n - 1], nums[i] = n, nums[n - 1]
        for i, n in enumerate(nums):
            if n == i + 1: continue
            elif nums[n - 1] == n: result.append(n)
        return result

def test():
    solution = Solution()

    assert sorted(solution.findDuplicates([])) == []
    assert sorted(solution.findDuplicates([1])) == []
    assert sorted(solution.findDuplicates([3, 3, 1])) == [3]
    assert sorted(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])) == [2, 3]
    print("self test passed")

if __name__ == '__main__':
    test()
