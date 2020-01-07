#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

==============================================================================================
SOLUTION

Tree/graph traversal problem.

The recurrence relation is about the all sub-paths starting from a node to left.

1. Recursion search

2. Iterative search

'''

from _tree import TreeNode, Codec

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = self._binaryTreePathsRecursion(root)
        print(paths)
        return paths

    def _binaryTreePathsRecursion(self, root: TreeNode):
        def dfs(node):
            paths = []
            if not node:
                return paths
            for child in (node.left, node.right):
                subPaths = child and dfs(child)
                if not subPaths:
                    continue
                for subPath in subPaths:
                    paths.append([str(node.val)] + subPath)
            if not paths:
                paths.append([str(node.val)])
            return paths
        result = ['->'.join(path) for path in dfs(root)]
        return result

    def _binaryTreePathsIteration(self, root: TreeNode):
        # TODO: do it iteratively
        pass

def test():
    """TODO: Docstring for test.
    :returns: TODO

    """

    solution = Solution()

    assert sorted(solution.binaryTreePaths(Codec.deserialize('[]'))) == []
    assert sorted(solution.binaryTreePaths(Codec.deserialize('[1]'))) == ['1']
    assert sorted(solution.binaryTreePaths(Codec.deserialize('[1,2,null,3,null,4,null]'))) == ['1->2->3->4']
    assert sorted(solution.binaryTreePaths(Codec.deserialize('[1,2,3,null,5]', int))) == ["1->2->5", "1->3"]

    print("self test passed")

if __name__ == '__main__':
    test()
