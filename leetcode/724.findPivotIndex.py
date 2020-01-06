#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
724. Find Pivot Index

Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
Input:
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:
Input:
nums = [1, 2, 3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Note:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].

==============================================================================================
SOLUTION

1. Brute force
Exhaust all indices, and verify its left sum and right sum.

Complexity: O(N²), O(1)

2. Prefix sum
Compute prefix sum cumulating from left and prefix cumulating from right, the target index is
the one with both equal value of sums on both side.

Complexity: O(N), O(N)

3. Prefix sum optimized

Compute both left prefix sum and right prefix sum on the fly, incrementally!

And, condition left = right, can be transformed to left - right = 0. Tracking the difference
will reduce the potential overflow and optimize a little bit.

Complexity: O(N), O(1)

"""

class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = self._pivotIndexPrefixSum(nums)

        print(nums, result)

        return result

    def _pivotIndexPrefixSum(self, nums):
        pivot = -1
        diff = -sum(nums)
        for i in range(len(nums)):
            diff += nums[i]
            if diff == 0:
                pivot = i
                break
            diff += nums[i]
        return pivot

def test():
    solution = Solution()

    nums = []
    assert solution.pivotIndex(nums) == -1

    nums = [1]
    assert solution.pivotIndex(nums) == 0

    nums = [0, 1]
    assert solution.pivotIndex(nums) == 1

    nums = [1, 0, 0, 0, 1]
    assert solution.pivotIndex(nums) == 1

    nums = [1, 7, 3, 6, 5, 6] # -28, -26, -12, -6, 6
    assert solution.pivotIndex(nums) == 3

    print("self test passed")


if __name__ == "__main__":
    test()
