#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Total Accepted: 82444
Total Submissions: 270772
Difficulty: Medium
Contributors: Admin


Note:
You may assume that duplicates do not exist in the tree.

==============================================================================================
SOLUTION:
    First, analyze the situation.
    preorder: root, left, right.
    inorder:  left, root, right.

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

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeDFS(
            preorder, inorder,
            (0, len(preorder) - 1), (0, len(preorder) - 1))

    def buildTreeDFS(self, preorder: list, inorder: list,
                     r1, r2) -> TreeNode:
        '''
        r1: preorder range tuple
        r2: inorder range tuple
        '''
        if r1[0] > r1[1]:
            return None
        # FIXME: slice is slow and creates new objects. Passing indices instead!
        # TODO: Still, speed it up looking up root's position in inorder sequence
        root = TreeNode(preorder[r1[0]])
        idx = inorder.index(root.val) - r2[0] # current root index offset
        root.left = self.buildTreeDFS(preorder, inorder,
                                      (r1[0] + 1, r1[0] + idx), (r2[0], r2[0] + idx - 1))
        root.right = self.buildTreeDFS(preorder, inorder,
                                       (r1[0] + idx + 1, r1[1]), (r2[0] + idx + 1, r2[1]))
        return root

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = solution.buildTree([], [])
    assert Codec.serialize(root) == '[]'

    root = solution.buildTree([-3], [-3])
    assert Codec.serialize(root) == '[-3]'

    root = solution.buildTree([1, 2, 3], [2, 1, 3])
    assert Codec.serialize(root) == "[1,2,3]"

    root = solution.buildTree([3, 5, 6, 2, 7, 4, 1, 0, 8],
                              [6, 5, 7, 2, 4, 3, 0, 1, 8])
    assert Codec.serialize(root) == '[3,5,1,6,2,0,8,null,null,7,4]'

    root = solution.buildTree([1, 2, 3, -4, 5], [2, 1, -4, 3, 5])
    assert Codec.serialize(root) == '[1,2,3,null,null,-4,5]'

    print('self test passed')

if __name__ == '__main__':
    test()
