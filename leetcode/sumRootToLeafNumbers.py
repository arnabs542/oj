#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
129. Sum Root to Leaf Numbers

Total Accepted: 94187
Total Submissions: 271281
Difficulty: Medium
Contributors: Admin

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent
a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        paths = self.sumNumbersBFS(root)
        return sum(paths)

    def sumNumbersBFS(self, root):
        '''
        Store paths while breadth-first searching
        '''
        paths = []
        frontier = [[root]] if root else []
        while frontier:
            path = frontier.pop(0)
            node = path[-1]
            for child in (node.left, node.right):
                if child:
                    frontier.append(path + [child])
            if not (node.left or node.right):
                # paths.append(list(map(lambda x: x.val, path)))
                num = 0
                for n in path:
                    num = num * 10 + n.val
                paths.append(num)

        print(paths)
        return paths

    # TODO: maybe DFS, such as preorder traversal

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert not solution.sumNumbers(root)

    root = Codec.deserialize("[1,2,3]", int)
    assert solution.sumNumbers(root) == 25

    root = Codec.deserialize('[1,null,2,null,3]', int)
    assert solution.sumNumbers(root) == 123

test()
