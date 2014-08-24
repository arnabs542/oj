# -*- coding:utf-8 -*-

'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def __init__(self):
        self.visit = []

    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root is not None:
            self.visit.append(root.val)
            if root.left is not None:
                self.preorderTraversal(root.left)
            if root.right is not None:
                self.preorderTraversal(root.right)

        return self.visit
