#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
449. Serialize and Deserialize BST

Total Accepted: 1610
Total Submissions: 4084
Difficulty: Medium
Contributors: ben65

Serialization is the process of converting a data structure or object into a sequence
of bits so that it can be stored in a file or memory buffer, or transmitted across a
network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no
restriction on how your serialization/deserialization algorithm should work. You just need
to ensure that a binary search tree can be serialized to a string and this string can be
deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states. Your serialize and
deserialize algorithms should be stateless.

==============================================================================================
SOLUTION:
    Copy from 'Serialize and Deserialize Binary Tree'
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []
        frontier = [root]
        while frontier:
            vertex = frontier.pop(0)
            data.append(str(vertex.val) if vertex else 'null')
            if vertex:
                frontier.append(vertex.left)
                frontier.append(vertex.right)

        while data and data[-1] == 'null': data.pop()
        # print('BFS result:', data)
        return '[{}]'.format(','.join(data))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vertices = [TreeNode(x.strip()) if x not in ('', 'null') else None
                    for x in data.strip("[]").split(',')]

        root = vertices.pop(0) if vertices else None
        frontier = [root] if root else []
        while frontier and vertices:
            vertex = frontier.pop(0)
            vertex.left, vertex.right = (vertices.pop(0) if vertices else None,
                                         vertices.pop(0) if vertices else None)
            for child in (vertex.left, vertex.right):
                if child: frontier.append(child)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
