#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
112. Path Sum

Total Accepted: 131669
Total Submissions: 404092
Difficulty: Easy
Contributors: Admin

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :typ, s: int
        :rtype: bool
        """
        print(root, s)
        return root is not None and (
            root.val == s and not root.left and not root.right
            or
            self.hasPathSum(root.left, s - root.val)
            or
            self.hasPathSum(root.right, s - root.val))


def test():

    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize("[5,4,8,11,null,13,4,7,2,null,null,null,1]", int)
    assert solution.hasPathSum(root, 22)

    root = Codec.deserialize("[]", int)
    assert not solution.hasPathSum(root, 1)

    print('self test passed')
    pass

test()
