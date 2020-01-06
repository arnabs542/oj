#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
110. Balanced Binary Tree

Total Accepted: 142078
Total Submissions: 396276
Difficulty: Easy
Contributors: Admin

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root: TreeNode) -> int:
        """
        return root node's height if its balanced, else -1
        """
        if not root:
            return 0
        left = self.dfsHeight(root.left)
        right = self.dfsHeight(root.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize('[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]', int)
    assert solution.isBalanced(root)

    root = Codec.deserialize('[]', int)
    assert solution.isBalanced(root)
    root = Codec.deserialize('[3,9,20,null,null,15,7]', int)
    assert solution.isBalanced(root)

    root = Codec.deserialize('[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]', int)
    assert solution.isBalanced(root)

    print('self test passed')
    pass

if __name__ == '__main__':
    test()
