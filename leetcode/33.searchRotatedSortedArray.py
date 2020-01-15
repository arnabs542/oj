#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
33. Search in Rotated Sorted Array

Total Accepted: 137787
Total Submissions: 432668
Difficulty: Hard
Contributors: Admin

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

==============================================================================================
SOLUTION


1. Binary search with more condition

Analyze the divided sub-spaces while we are dividing the array.

A sorted array is divided into TWO DISJOINT INCREASING subarrays after rotated:
    a₁a₂...aₘb₁b₂...bₚ, where a₁ >= b₂.

In normal binary search, space is split into two non-overlapping interval.
In this situation, we need to know at least one sub-space value range!
And the truth is, at least one half is sorted!

1) Find middle point mid = (l + h)/2
2) If key is present at middle point, return mid.
3) Else If arr[l..mid] is sorted
    a) If key to be searched lies in range from arr[l]
       to arr[mid], recur for arr[l..mid].
    b) Else recur for arr[mid+1..h]
4) Else (arr[mid+1..h] must be sorted)
    a) If key to be searched lies in range from arr[mid+1]
       to arr[h], recur for arr[mid+1..h].
    b) Else recur for arr[l..mid]
Of course, we can add pruning?


2. Find the pivot point first with binary search, then perform normal binary search
Then for each comparison in binary search, we need to determine where the pivot is.
The pivot k has nums[k-1] > nums[k] <= nums[k+1].
One exception is nums[k-1] == nums[k] so that all numbers are the same.
0) Middle is the pivot: found!
1) Middle > nums[0]: go right
2) Middle < nums[n-1]: to left

Special case is the array is not rotated, then in this case nums[0] <= nums[n-1].

TODO: find pivot with binary search first.

Complexity: O(logN), three passes of binary search in total.

FOLLOW UP
================================================================================
81. Search in Rotated Sorted Array II
Duplicate numbers exist.


'''

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = self.searchBinarySearch(nums, target)

        print(nums, target, result)

        return result

    def searchBinarySearch(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[high]:  # two cases
                if nums[mid] < target <= nums[high]:  # different range
                    low = mid + 1
                else:
                    high = mid - 1
            else: # nums[mid] > nums[high]
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            pass
        return -1

def test():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 2) == 6
    assert Solution().search([5, 1, 2, 3, 4], 1) == 1
    assert Solution().search([5, 6, 7, 8, 9, 1, 2, 3, 4], 2) == 6

    print("self test passed")

if __name__ == "__main__":
    test()
