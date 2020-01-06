#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
18. 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

================================================================================
SOLUTION

1. Brute force

Complexity: O(N⁴)

2. Two pointers

Reduce the problem two two pointers!

Complexity: O(nlogn) + O(n²n) = O(n³)

"""


class Solution(object):

    def nSum(self, nums, target, n=2, sort=False):
        """
        :param nums: List[int]
        :param target: int
        :param n: int
        :param sort: bool

        :return: List[List[int]]
        """
        if sort:
            # only sort once
            nums.sort()
        if n < 2 or len(nums) < n or target < nums[0] * n or target > nums[-1] * n:
            # early stop
            return
        if n == 2:
            # DONE: two pointers algorithm when n is 2
            low, high = 0, len(nums) - 1
            while low < high:
                curr_sum = nums[low] + nums[high]
                if curr_sum < target:
                    low += 1
                elif curr_sum == target:
                    yield (nums[low], nums[high])
                    while low < high:
                        if nums[low] == nums[low + 1]:
                            low += 1
                        elif nums[high] == nums[high - 1]:
                            high -= 1
                        else:
                            break
                    low += 1
                    high -= 1
                else:
                    high -= 1
        else:
            for i in range(len(nums) - n + 1):
                if i and nums[i] == nums[i - 1]:
                    # avoid duplicate tuples
                    continue
                # XXX: RECURSIVELY reduce n by 1
                for t in self.nSum(nums[i + 1:], target - nums[i], n - 1):
                    yield (nums[i],) + t

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        return list(self.nSum(nums, target, n=4, sort=True))

def test():
    solution = Solution()

    print("self test passed!")

if __name__ == '__main__':
    test()
