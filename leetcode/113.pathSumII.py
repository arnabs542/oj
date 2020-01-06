#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
113. Path Sum II

Total Accepted: 103058
Total Submissions: 334818
Difficulty: Medium
Contributors: Admin

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum
equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

================================================================================
SOLUTION

1. Depth-first search, recursion

'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(node, target, path):
            if not node:
                return
            if node.val == target and not (node.left or node.right): # equal, and leaf
                result.append(list(path + [node.val]))
            else:
                path.append(node.val)
                dfs(node.left, target - node.val, path)
                dfs(node.right, target - node.val, path)
                path.pop()
            pass

        path = []
        dfs(root, sum, path)

        print(result)
        return result

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.pathSum(root, 1) == []

    root = Codec.deserialize('[1,null,2,null,3,null,4,null,5]', int)
    assert solution.pathSum(root, 15) == [[1, 2, 3, 4, 5]]

    print('self test passed')
    pass

if __name__ == '__main__':
    test()
