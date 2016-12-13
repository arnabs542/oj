#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
162. Find Peak Element

Total Accepted: 92002
Total Submissions: 258958
Difficulty: Medium
Contributors: Admin

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the
peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return
the index number 2.

Note:
Your solution should be in logarithmic complexity.

==============================================================================================
SOLUTION:
1. Naive solution: linear scan

2. Logarithm solution?

First, analyze the MONOTONICITY of array.
Assume we have divided the array into groups of ascending or descending subarrays like this:
    .../\/\/\/\/\/\/\/\/...
Where "/" denotes ascending sequence, and "\\" denotes descending sequence.

Take arbitrary two numbers nums[i] and nums[i + 1], then we have the observation:
        if nums[i] > nums[i + 1], then a peak element can be found in range [0, i],
        and vice versa
Proof:
    If nums[i] > nums[i + 1], then nums[i] must be part of an ascending or descending subarray.
Denote the subarray by `A`, and its beginning is nums[j].
If A is descending, then there are two scenarios:
    1) j == 0: nums[j] is a peak, because nums[-1] = -∞ < nums[j] > nums[j + 1]
    2) j > 0: nums[j - 1] < nums[j] > nums[j + 1]
So nums[j] is a peak element.

If A is ascending, then:
    nums[i - 1] < nums[i] > num[i + 1], so i is a peak.

Given that, we can REPEATEDLY DIVIDING the array by 2 into two ranges, to find such a peak,
just as Binary Search.

'''

class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return self.findPeakElementLinear(nums)
        return self.findPeakElementLog(nums)

    def findPeakElementLinear(self, nums: list) -> int:
        for i, _ in enumerate(nums):
            if (i == 0 or nums[i] > nums[i - 1])\
               and (i == len(nums) - 1 or nums[i] > nums[i + 1]):
                return i
        return -1

    def findPeakElementLog(self, nums: list) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            # print(nums, low, high, mid)
            if (mid == 0 or nums[mid] > nums[mid - 1]) and \
               (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif (mid < len(nums) - 1 and nums[mid] < nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1

        return -1

def test():
    solution = Solution()

    assert solution.findPeakElement([]) == -1
    assert solution.findPeakElement([1]) == 0
    assert solution.findPeakElement([1, 1]) == -1
    assert solution.findPeakElement([1, 2]) == 1
    assert solution.findPeakElement([1, 2, 3, 1]) == 2

    print('self test passed')

if __name__ == '__main__':
    test()
