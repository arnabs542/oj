#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
226. Invert Binary Tree

Total Accepted: 136901
Total Submissions: 277975
Difficulty: Easy
Contributors: Admin
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
    Google: 90% of our engineers use the software you wrote (Homebrew), but you
    can’t invert a binary tree on a whiteboard so fuck off.

==============================================================================================
SOLUTION:
    Hi, Google, I can invert a binary tree!
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.invertTreeRecursive(root)

    def invertTreeRecursive(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return node
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            return node

        return dfs(root)
