#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
235. Lowest Common Ancestor of a Binary Search Tree

Total Accepted: 103409
Total Submissions: 273124
Difficulty: Easy
Contributors: Admin

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given
nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has both v and w as descendants (
where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is
LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the
LCA definition.
===============================================================================================
SOLUTION:
    1. parent pointer
    2. recursively traverse the root of the binary search tree.
        2.1 store paths to nodes
        2.2 utilize the binary search tree's property: left is smaller and right is greater
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            # If both n1 and n2 are greater than root, then LCA lies in right
            if root.val < p and root.val < q:
                root = root.right
            # If both n1 and n2 are smaller than root, then LCA lies in left
            elif root.val > p and root.val > q:
                root = root.left
            else:
                break

        return root
