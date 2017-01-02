#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
230. Kth Smallest Element in a BST

Total Accepted: 78213
Total Submissions: 187183
Difficulty: Medium
Contributors: Admin

Given a binary search tree, write a function kth Smallest to find the kth smallest
element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the
kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

1. Try to utilize the property of a BST.
2. What if you could modify the BST node's structure?
3. The optimal runtime complexity is O(height of BST).

==============================================================================================
SOLUTION

1. Inorder traversal: get the smallest for k times.

2. Binary Search
Compute the number of nodes on the left and right side, and determine which branch contains
the kth element. To compute the number of nodes in a BST takes time complexity of O(N).

3. But if we can modify the BST nodes' structure, add a count field in the BST node class,
so that we can query kth smallest with binary search, O(logN). And the insertion, deletion
take O(logN) time complexity.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.kthSmallestInorder(root, k)

    def kthSmallestInorder(self, root, k):
        stack = []
        while k:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop() if stack else None
            k -= 1
            if k and root: root = root.right
            else: return root.val if root else None
        return None

from serializeAndDeserializeBinaryTree import Codec

def test():
    solution = Solution()

    assert solution.kthSmallest(Codec.deserialize("[1]", int), 1) == 1
    assert solution.kthSmallest(Codec.deserialize("[2,1,3]", int), 2) == 2
    assert solution.kthSmallest(Codec.deserialize("[2,1,3]", int), 3) == 3
    assert solution.kthSmallest(Codec.deserialize("[2,1,3]", int), 6) == None

    print("self test passed")

if __name__ == '__main__':
    test()

