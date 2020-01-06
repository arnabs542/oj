#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
81. Search in Rotated Sorted Array II

Total Accepted: 80363
Total Submissions: 244350
Difficulty: Medium
Contributors: Admin

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

==============================================================================================
SOLUTION

Binary Search with duplicate number.

Pay attention to the scenario where the middle value is equal to an end value. In this
case, the range division is undetermined, but we can at least reduce the range by one,
moving the right end left by one.


'''

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return bool(mid)
            elif nums[mid] < nums[high]:  # two cases
                if nums[mid] < target <= nums[high]:  # different range
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] == nums[high]:
                high -= 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            pass

        return False

def test():
    assert Solution().search([4, 5, 6, 7, 0, 1, 2], 2) == bool(6)
    assert Solution().search([5, 1, 2, 3, 4], 1) == bool(1)
    assert Solution().search([5, 6, 7, 8, 9, 1, 2, 3, 4], 2) == bool(6)

    print("self test passed")

if __name__ == "__main__":
    test()
