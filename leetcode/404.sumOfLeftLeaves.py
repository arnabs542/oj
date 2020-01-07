#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

==============================================================================================
SOLUTION

For an arbitrary node in the tree, its sum of all left leaves is in two scenarios:
    1) value itself if it's a leaf
    2) sum of all left leaves of its children(left and right node)

1. Recursive solution

The recurrence relation involves state of two tuple: (sum of all left leaves, is leaf or not).

2. Iterative: bfs or dfs

During the gragh search process, we need to store not only the nodes, but also an extra flag
state indicating whether it's a left child or not.

state = (node, whether it's left child or not)

Also, we can do this in another manner:
    Put nodes in the frame, check whether its left child is a leaf. And push non-leaf children
into the stack. state = (node)

'''

from _tree import Codec, TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self._sumOfLeftLeavesDfs(root)

    def _sumOfLeftLeavesDfs(self, root: TreeNode):
        def dfs(node):
            result = [0, False] # [sum of left leaves, is leaf]
            if not node:
                return [0, False]
            ret = dfs(node.left)
            result[0] += ret[0] if not ret[1] else node.left.val
            result[0] += dfs(node.right)[0]
            result[1] = not (node.left or node.right) # is leaf

            # print('node: ', node, result)
            return result

        return dfs(root)[0] or 0

    # TODO: iterative solution

def test():

    solution = Solution()

    root = Codec.deserialize('[]')
    assert solution.sumOfLeftLeaves(root) == 0

    root = Codec.deserialize('[3,9,20,null,null,15,7]', int)
    assert solution.sumOfLeftLeaves(root) == 24

    root = Codec.deserialize('[3,9,20,1,5,15,7]', int)
    assert solution.sumOfLeftLeaves(root) == 16

    root = Codec.deserialize('[3,9,20,1,5,15,7,null,null,2]', int)
    assert solution.sumOfLeftLeaves(root) == 18

    root = Codec.deserialize('[3,9,20,1,5,15,7,null,null,null,2]', int)
    assert solution.sumOfLeftLeaves(root) == 16

    print("self test passed")

if __name__ == '__main__':
    test()
