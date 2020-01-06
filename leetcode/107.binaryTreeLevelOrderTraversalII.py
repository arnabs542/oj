#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
107. Binary Tree Level Order Traversal II

Total Accepted: 103941
Total Submissions: 280566
Difficulty: Easy
Contributors: Admin

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result, frontier, frontier_new = [], [root] if root else [], []
        while frontier:
            result.append([])
            while frontier:
                node = frontier.pop(0)
                result[-1].append(node.val)
                for child in (node.left, node.right):
                    if child:
                        frontier_new.append(child)
                pass
            frontier_new, frontier = frontier, frontier_new
        print(result)
        return result[::-1]
