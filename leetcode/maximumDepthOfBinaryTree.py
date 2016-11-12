#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
104. Maximum Depth of Binary Tree

Total Accepted: 192238
Total Submissions: 382439
Difficulty: Easy
Contributors: Admin

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node
down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        frontier, frontier_new = [root] if root else [], []
        depth = 0
        while frontier:
            depth += 1
            while frontier:
                node = frontier.pop(0)
                for child in (node.left, node.right):
                    if child: frontier_new.append(child)
            frontier, frontier_new = frontier_new, frontier

        return depth
