#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
297. Serialize and Deserialize Binary Tree

Total Accepted: 36380
Total Submissions: 118822
Difficulty: Hard
Contributors: Admin

Serialization is the process of converting a data structure or object into a sequence of
bits so that it can be stored in a file or memory buffer, or transmitted across a network
connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on
how your serialization/deserialization algorithm should work. You just need to ensure that
a binary tree can be serialized to a string and this string can be deserialized to the
original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You
do not necessarily need to follow this format, so please be creative and come up with
different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and
deserialize algorithms should be stateless.

==============================================================================================
SOLUTION

1. Breadth-first search traversal

2. Depth-first search traversal

'''

import re

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'val = {}'.format(self.val)

class Codec:

    debug = False

    @classmethod
    def serialize(cls, root, debug=False):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        cls.debug = debug
        serializedTree = cls._serializeBFS(root)
        if cls.debug:
            print(serializedTree)
        return serializedTree

    @classmethod
    def deserialize(cls, data: str,
                    T: type=str, NodeType: type=TreeNode, debug=False):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        cls.debug = debug
        root = cls._deserializeBFS(data, T, NodeType)
        if debug:
            cls.drawtree(root)
        return root

    @classmethod
    def _serializeBFS(cls, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        Breadth-first search.
        """
        data = []
        frontier = [root]
        while frontier:
            vertex = frontier.pop(0)
            data.append(str(vertex.val) if vertex else 'null')
            if vertex:
                frontier.append(vertex.left)
                frontier.append(vertex.right)
            pass

        while data and data[-1] == 'null': data.pop()
        # print('BFS result:', data)
        return '[{}]'.format(','.join(data))

    @classmethod
    def _deserializeBFS(cls, data, T: type=str, NodeType: type=TreeNode):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        Breadth-first search.
        """
        # strip the parentheses
        vertices = [NodeType(T(x.strip())) if x not in ('', 'null', ' null', '#', ' #') else None
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

    @classmethod
    def _serializeDFS(cls, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # TODO: depth-first solution

    @classmethod
    def _deserializeInorder(cls, root: TreeNode) -> TreeNode:
        # guess at least another traversal sequence is necessary
        pass

    @classmethod
    def _serializeInorder(cls, root):
        pass

    @staticmethod
    def drawtree(root):
        # TODO: visualize tree
        pass

# Your Codec object will be instantiated and called as such:
def test():
    codec = Codec()

    root = codec.deserialize("[]")
    assert codec.serialize(root, debug=True) == "[]"

    assert codec.serialize(codec.deserialize("[1,2]"), debug=True) == "[1,2]"
    assert codec.serialize(codec.deserialize("[1,2,3]"), debug=True) == "[1,2,3]"

    root = codec.deserialize("[1, 2, 3, null,null,4,5]", debug=True)
    assert codec.serialize(root, debug=True) == "[1,2,3,null,null,4,5]"

    root = codec.deserialize("[null,2,3,null,null,4,5]", debug=True)
    assert codec.serialize(root, debug=True) == "[]"

    print('self test passed')


if __name__ == '__main__':
    test()
