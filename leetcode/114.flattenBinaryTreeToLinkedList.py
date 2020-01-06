#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
114. Flatten Binary Tree to Linked List

Total Accepted: 105084
Total Submissions: 316296
Difficulty: Medium
Contributors: Admin

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
    If you notice carefully in the flattened tree, each node's right child points
to the next node of a pre-order traversal.
'''
from serializeAndDeserializeBinaryTree import TreeNode, Codec

# Definition for a binary tree node.
# class TreeNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.left = None
        # self.right = None

class Solution(object):

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        return self.flattenRecursive(root)

    def flattenRecursive(self, root: TreeNode):
        def dfs(node: TreeNode):
            '''
            return STATE = (head, tail) of current subtree
            '''
            if not node:
                return None, None
            if not (node.left or node.right):
                return node, node
            left, right = dfs(node.left), dfs(node.right)
            node.left = None
            node.right = left[0] or right[0]
            if left[1]: left[1].right = right[0]

            return node, right[1] or left[1] or node
        return dfs(root)[0]

def test():
    solution = Solution()

    root = Codec.deserialize('[]')
    assert Codec.serialize(solution.flatten(root)) == '[]'

    root = Codec.deserialize('[1]')
    assert Codec.serialize(solution.flatten(root)) == '[1]'

    root = Codec.deserialize('[1,2,3]')
    r = Codec.serialize(solution.flatten(root))
    print(r)
    assert r == '[1,null,2,null,3]'

    root = Codec.deserialize('[1,2]')
    r = Codec.serialize(solution.flatten(root))
    print(r)
    assert r == '[1,null,2]'

    root = Codec.deserialize('[1,2,null,3,null,4]')
    r = Codec.serialize(solution.flatten(root))
    print(r)
    assert r == '[1,null,2,null,3,null,4]'

    root = Codec.deserialize('[1,2,3,4]')
    r = Codec.serialize(solution.flatten(root))
    print(r)
    assert r == '[1,null,2,null,4,null,3]'

    root = Codec.deserialize('[1,2,5,3,4,null,6]')
    assert Codec.serialize(solution.flatten(root)) == '[1,null,2,null,3,null,4,null,5,null,6]'

    print('self test passed')

if __name__ == '__main__':
    test()
