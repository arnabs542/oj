#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
106. Construct Binary Tree from Inorder and Postorder Traversal

Total Accepted: 70555
Total Submissions: 229987
Difficulty: Medium
Contributors: Admin

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

==============================================================================================
SOLUTION:
    First, analyze the situation.
    inorder:  left, root, right.
    postorder: left, right, root.

    Then the first occurrence in preorder traversal sequence is the ROOT. And we can use it
to split inorder sequence to separate left and right subtree sequences. The following will be
'DIVIDE AND CONQUER'( a RECURSIVE PROCEDURE).
'''
# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeDFS(
            inorder, postorder,
            (0, len(inorder) - 1), (0, len(inorder) - 1))

    def buildTreeDFS(self, inorder: list, postorder: list,
                     r1, r2) -> TreeNode:
        '''
        r1: inorder range tuple
        r2: inorder range tuple
        '''
        if r1[0] > r1[1]:
            return None
        root = TreeNode(postorder[r2[1]])
        idx = inorder.index(root.val) - r1[0]  # current root index offset
        root.left = self.buildTreeDFS(inorder, postorder,
                                      (r1[0], r1[0] + idx - 1), (r2[0], r2[0] + idx - 1))
        root.right = self.buildTreeDFS(inorder, postorder,
                                       (r1[0] + idx + 1, r1[1]), (r2[0] + idx, r2[1] - 1))
        return root

def test():

    from _tree import Codec

    solution = Solution()

    root = solution.buildTree([], [])
    assert Codec.serialize(root) == '[]'

    root = solution.buildTree([-3], [-3])
    assert Codec.serialize(root) == '[-3]'

    root = solution.buildTree([2, 1, 3], [2, 3, 1])
    assert Codec.serialize(root) == "[1,2,3]"

    root = solution.buildTree([6, 5, 7, 2, 4, 3, 0, 1, 8],
                              [6, 7, 4, 2, 5, 0, 8, 1, 3])
    assert Codec.serialize(root) == '[3,5,1,6,2,0,8,null,null,7,4]'

    root = solution.buildTree([2, 1, -4, 3, 5], [2, -4, 5, 3, 1])
    assert Codec.serialize(root) == '[1,2,3,null,null,-4,5]'

    print('self test passed')

if __name__ == '__main__':
    test()
