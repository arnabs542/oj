#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
80. Remove Duplicates from Sorted Array II

Total Accepted: 95963
Total Submissions: 277844
Difficulty: Medium
Contributors: Admin

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being
1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

==============================================================================================
SOLUTION:
    TWO POINTERS PARTITIONING ALGORITHM.
'''

class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, dup = -1, 0
        for j, _ in enumerate(nums):
            if j and nums[j] == nums[j - 1]:
                dup += 1
            else:
                dup = 0
            if dup <= 1:
                i += 1
                nums[i] = nums[j]

        return i + 1

def test():
    solution = Solution()

    assert solution.removeDuplicates([]) == 0
    assert solution.removeDuplicates([1, 1, 2]) == 3
    assert solution.removeDuplicates([1, 1, 1]) == 2
    assert solution.removeDuplicates([1, 2, 3]) == 3

    print('self test passed')

if __name__ == '__main__':
    test()

