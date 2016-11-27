#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
95. Unique Binary Search Trees II

Total Accepted: 69928
Total Submissions: 230199
Difficulty: Medium
Contributors: Admin

Given an integer n, generate all structurally unique BST's (binary search trees) that
store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

==============================================================================================
SOLUTION:
    Of course, this is a Catalan Number problem.
    DIVIDE AND CONQUER to form STATE TRANSITION RELATION.

Given n, there are n - 1 nodes to construct except the root one. The we can divide the rest of
nodes by (0, n -1), (1, n - 1), ..., (n - 1, 0), in total n ways. In each way, we have a
corresponding subproblem with (optimal substructure).

1. Then this problem could be tackled with DEPTH-FIRST SEARCH approach.

2. To optimize the speed, we can reduce the duplicate calculations by memoization or bottom-up
DYNAMIC PROGRAMMING.

1) Iterate length in range(1, n), to get the unique trees with value from i to j in
2-dimensional state transition table trees[i][j].
2) Alternatively, use 1D table tree[j] to denotes the trees with elements from 0 to j. Then
in the bottom-up procedure, the right subtrees(n - 1 - j) can be obtained by cloning tree[n-j]
with value offset j + 1.
'''

from serializeAndDeserializeBinaryTree import Codec

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreesRecursive(n)

    def generateTreesRecursive(self, n: int) -> TreeNode:
        def dfs(nums: int, start: int, end: int):
            if start >= end:
                return [None]
            elif start + 1 == end:
                return [TreeNode(nums[start])]
            trees = []
            for i in range(start, end):
                left = dfs(nums, start, i)
                right = dfs(nums, i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(nums[i])
                        # TODO: deep copy the left and right subtree here
                        root.left = l
                        root.right = r
                        trees.append(root)
                    pass
            return trees

        return dfs(list(range(1, n + 1)), 0, n) if n > 0 else []

    def generateTreesDP(self, n: int) -> TreeNode:
        # TODO: Dynamic Programming approach

def test():
    solution = Solution()

    trees = solution.generateTrees(0)
    trees = [Codec.serialize(root) for root in trees]
    print(trees)
    assert trees == []

    trees = solution.generateTrees(1)
    trees = [Codec.serialize(root) for root in trees]
    print(trees)
    assert trees == ['[1]']

    trees = solution.generateTrees(2)
    trees = [Codec.serialize(root) for root in trees]
    print(trees)
    assert trees == ['[1,null,2]', '[2,1]']

    trees = solution.generateTrees(3)
    trees = [Codec.serialize(root) for root in trees]
    print(trees)
    assert trees == ['[1,null,2,null,3]', '[1,null,3,2]', '[2,1,3]', '[3,1,null,null,2]', '[3,2,null,1]']

if __name__ == '__main__':
    test()
