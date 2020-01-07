#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

==============================================================================================
SOLUTION

A tree, is a special graph with only forward edges, is a recursive structure.

Diameter is defined as the number of nodes on the path minus 1.

If we directly track the state as diameter, then there will be an ambiguity.
Both empty empty path and path with only one node will have same value of diameter. But, in the
state transition recurrence relation, we need to differentiate those two cases.
For example,  [] and [1] both have diameter of 0, but adding another node, this changes.
[2] and [1, 2] have diameter of 0 and 1 respectively!

Mathematically, denote the state transition function as f(state, action), we have:
    f(0, 1) = 0, and f(0, 1) = 1

The state transition function isn't well defined! Because it incorrectly map one variable to
two target values. Because choosing diameter as state will lose information.

So, CHOOSE STATE WITHOUT LOSING INFORMATION for STATE TRANSITION FUNCTION!

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self._diameterOfBinaryTreeDfs(root)

        print("result: ", result)

        return result

    def _diameterOfBinaryTreeDfs(self, root):
        def dfs(node):
            """
            Define state as a tuple of:
                max_so_far: globally maximum number of nodes on a path
                max_ending_here: maximum number of nodes on path ending here
            """
            if not node:
                return 0, 0
            max_so_far_left, max_ending_here_left = dfs(node.left)
            max_so_far_right, max_ending_here_right = dfs(node.right)

            max_so_far = max(1 + max_ending_here_left + max_ending_here_right,
                             max_so_far_left,
                             max_so_far_right
                            )
            max_ending_here = max(max_ending_here_left, max_ending_here_right) + 1
            return max_so_far, max_ending_here

        def dfs1(node):
            """
            Define state as a tuple of:
                max_so_far: globally optimal solution
                max_ending_here: maximum number of nodes on path ending here
            """
            if not node:
                return 0, 0
            max_so_far_left, max_ending_here_left = dfs(node.left)
            max_so_far_right, max_ending_here_right = dfs(node.right)

            max_so_far = max(max_ending_here_left + max_ending_here_right,
                             max_so_far_left,
                             max_so_far_right
                            )
            max_ending_here = max(max_ending_here_left, max_ending_here_right) + 1
            return max_so_far, max_ending_here

        # result, _ = dfs(root)
        # return max(0, result - 1)

        result, _ = dfs1(root)
        return result


def test():
    solution = Solution()

    from _tree import Codec

    root = Codec.deserialize("[]")
    assert solution.diameterOfBinaryTree(root) == 0

    root = Codec.deserialize("[1]")
    assert solution.diameterOfBinaryTree(root) == 0

    root = Codec.deserialize("[1,2,3,4,5]")
    assert solution.diameterOfBinaryTree(root) == 3

    print("self test passed!")

if __name__ == '__main__':
    test()
