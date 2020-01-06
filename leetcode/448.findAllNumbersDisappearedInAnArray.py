#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear
twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list
does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]


==============================================================================================
SOLUTION

The numbers are given in range [1, n], then we can utilize bucket inplace.

1. Naive solution

2. Bucket
In the first pass, iterate through the list, put the value into right bucket in the list.
In the second pass, check those indices that are not consistent with their values.

Of course, we can mark those elements as negative using nums[nums[i] -1] = -nums[nums[i]-1]
in the first pass.

----------------------------------------------------------------------------------------------
Reference

Similar to problem firstMissingPositive.py.

'''

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = self._findDisappearedNumbersBucket(nums)
        print(result)
        return result

    def _findDisappearedNumbersBucket(self, nums):
        result = []
        i = 0
        while i < len(nums):
            n = nums[i]
            # print(nums[i], nums)
            if nums[n - 1] == n: # value in right bucket?
                i += 1
                continue
            nums[i], nums[n - 1] = nums[n - 1], nums[i]
        for i, n in enumerate(nums):
            if n != i + 1:
                result.append(i + 1)
        return result

def test():
    solution = Solution()

    assert solution.findDisappearedNumbers([]) == []
    assert solution.findDisappearedNumbers([1]) == []
    assert solution.findDisappearedNumbers([2, 2]) == [1]
    assert solution.findDisappearedNumbers([1, 1]) == [2]
    assert solution.findDisappearedNumbers([2, 1]) == []
    assert solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]

    print("self test passed")

if __name__ == '__main__':
    test()
