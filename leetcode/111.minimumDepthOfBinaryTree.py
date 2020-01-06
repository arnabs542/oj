#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
111. Minimum Depth of Binary Tree

Total Accepted: 135977
Total Submissions: 425584
Difficulty: Easy
Contributors: Admin

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node
down to the nearest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def minDepth(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        frontier, frontier_new = [root] if root else [], []
        depth = len(frontier)
        while frontier:
            while frontier:
                node = frontier.pop(0)
                if not (node.left or node.right):
                    return depth
                else:
                    for child in (node.left, node.right):
                        if child: frontier_new.append(child)
            frontier, frontier_new = frontier_new, frontier
            depth += 1

        return depth
