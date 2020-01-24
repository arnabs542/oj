#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
16. 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

================================================================================
1. Brute force

Complexity: O(N³)

2. Sort and use two pointers - reducing the two sum closest

Complexity:  O(N²) + O(NlogN) = O(N²)

"""


class Solution(object):

    def twoSumClosest(self, nums, target):
        low, high = 0, len(nums) - 1

        closest_diff = None
        closest_integers = ()
        # print('target: ', target, nums)

        while low < high:
            diff = nums[low] + nums[high] - target
            # print(nums[low], nums[high], diff, closest_diff)
            if not closest_diff or closest_diff > abs(diff):
                closest_diff = abs(diff)
                closest_integers = (nums[low], nums[high],)
            if diff < 0:
                low += 1
            elif diff == 0:
                closest_diff = 0
                closest_integers = (nums[low], nums[high],)
                return closest_diff, closest_integers
            else:
                high -= 1

        return closest_diff, closest_integers

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

        closest_diff = None
        closest_integers = ()

        for i in range(len(nums) - 2):
            diff, integers = self.twoSumClosest(nums[i + 1:], target - nums[i])
            if not closest_diff or closest_diff > diff:
                closest_diff = diff
                closest_integers = (nums[i],) + integers
                if closest_diff == 0:
                    return sum(closest_integers)

        # print('solution: ', closest_diff, closest_integers)
        return sum(closest_integers)

def test():
    solution = Solution()

    assert solution.threeSumClosest([0, 0, 0], 1) == 0
    assert solution.threeSumClosest([1,1,-1,-1,3], 1) == 1
    assert solution.threeSumClosest([0, 2, 1, -3], 1) == 0
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2
    print('self test passed!')

    print("self test passed!")

if __name__ == '__main__':
    test()
