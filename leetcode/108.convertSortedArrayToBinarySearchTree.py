#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
108. Convert Sorted Array to Binary Search Tree

Total Accepted: 106820
Total Submissions: 262256
Difficulty: Easy
Contributors: Admin

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

==============================================================================================
SOLUTION


'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTRecursion(nums)

    def sortedArrayToBSTRecursion(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid]) if mid else None
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

def test():

    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize('[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]', int)
    assert not solution.sortedArrayToBST([])

    root = solution.sortedArrayToBST([1])
    print(Codec.serialize(root, int))

    root = solution.sortedArrayToBST([1, 2])
    print(Codec.serialize(root, int))

    root = solution.sortedArrayToBST([1, 2, 3])
    print(Codec.serialize(root, int))

    root = solution.sortedArrayToBST([1, 2, 3, 4])
    print(Codec.serialize(root, int))

    print('self test passed')

if __name__ == '__main__':
    test()
