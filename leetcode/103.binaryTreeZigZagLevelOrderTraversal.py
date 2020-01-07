#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
103. Binary Tree Zigzag Level Order Traversal

Total Accepted: 79006
Total Submissions: 250695
Difficulty: Medium
Contributors: Admin

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie,
from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        frontier, frontier_new = [root] if root else [], []
        while frontier:
            result.append([])
            # print(depth, frontier)
            while frontier:
                node = frontier.pop(0)
                for child in (node.left, node.right):
                    if child: frontier_new.append(child)
                result[-1].insert(len(result[-1]) if len(result) % 2 else 0, node.val)
            frontier, frontier_new = frontier_new, frontier

        print(result)
        return result

def test():

    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize("[3,9,20,null,null,15,7]", int)
    assert solution.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]

    root = Codec.deserialize('[3,9,20,null,null,15,7,4,10]', int)
    assert solution.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7], [10, 4]]

    root = Codec.deserialize('[1,2,3,4,null,null,5]', int)
    assert solution.zigzagLevelOrder(root) == [[1], [3, 2], [4, 5]]

    root = Codec.deserialize('[1,2,3,4,5,6,7]', int)
    assert solution.zigzagLevelOrder(root) == [[1], [3, 2], [4, 5, 6, 7]]

    print('self test passed')
    pass

test()
