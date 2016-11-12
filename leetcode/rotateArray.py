#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
189. Rotate Array   QuestionEditorial Solution  My Submissions
Total Accepted: 96377
Total Submissions: 420656
Difficulty: Easy
Contributors: Admin
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?

Related problem: Reverse Words in a String II
'''

class Solution(object):

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        return self.rotateSlice(nums, k)

    def rotateInsert(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            nums.insert(0, nums.pop())

    def rotateSlice(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

def test():
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    print('self test passed')
    pass

if __name__ == '__main__':
    test()
