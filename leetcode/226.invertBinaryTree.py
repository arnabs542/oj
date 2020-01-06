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

    # copy a invert of a binary tree
    def getMirror(self, root):
        def dfs(node):
            if not node:
              return None
            newNode = TreeNode(node.val)
            # mirror
            newNode.left = dfs(node.right)
            newNode.right = dfs(node.left)
            return newNode

        newRoot = dfs(root)

        return newRoot

    # TODO: test it
    def inverTreeIterative(self, root: TreeNode) -> TreeNode:
        """
        Get a mirror/invert of a binary tree
        """
        # in: node; local: childIdx, out: newNode
        # state = (node, childIdx, newNode)
        if not root:
            return None
        newRoot = TreeNode(root.val)
        stack = [(root, 0, newRoot)] # passing by reference

        while stack:
            node, i, newNode = stack[-1] # top element
            if i == 0:
                newNode.val = node.val
                i += 1
                stack.pop()
                stack.append((node, i + 1, newNode))
                state = (node.right, 0, TreeNode(0))
                stack.append(state)
            elif i == 1:
                stack.pop()
                stack.append(node, i + 1, newNode)
                # right child
                stack.append((node.left, 0, TreeNode(0)))
            elif i == 2:
                # time to pop out
                if stack:
                  node1, i1, newNode1 = stack[-1]
                  if i1 == 1:
                      newNode1.left = newNode
                  elif i1 == 2:
                      newNode1.right = newNode
        return newRoot
