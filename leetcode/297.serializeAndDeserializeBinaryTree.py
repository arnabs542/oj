#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
297. Serialize and Deserialize Binary Tree

Total Accepted: 36380
Total Submissions: 118822
Difficulty: Hard
Contributors: Admin

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.


SOLUTION
================================================================================

A tree structure can be deserialized using tree traversal(graph search with
breadth first search or depth first search).
But the problem is how to convert it from tree to string, back and forth.

Producing serialized string with tree traversing is straightforward.
To make it possible to convert it back to deserialized tree:
- Save NULL pointer nodes in the serialized string!
- Save 'end of children' marker in the serialized string(Space optimization)!

Explicitly keep the NULL nodes while serializing, so that different tree structure can't
have same traversal serialization. Then the ambiguity is resolved.

Procedure[serialize]:
The idea is to traverse the tree with dfs or bfs
For each vertex u,
    For each unvisited adjacent vertex v FROM THE TREE
      Put vertex v into the search frontier.
      Serialize vertex v.

Procedure[serialize]:
The idea is to traverse the tree with dfs or bfs
For each vertex u,
    For each unvisited adjacent vertex v constructed FROM THE STRING
      Put vertex v into the search frontier.

Takeaway
--------------------------------------------------------------------------------
Serialize and Deserialize are the same way to TRAVERSE the tree with bfs or dfs,
except the difference that in serialize adjacent nodes are retrieved FROM TREE
while in deserialize adjacent nodes must be constructed FROM THE STRING first.

1. Breadth-first search traversal
Complexity: O(n), O(N)

2. Depth-first search traversal - preorder
It can be done in both iterative and recursive approach.
Complexity: O(n), O(N)

TODO: dfs with inorder and postorder?

Reference:
https://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/


'''

import re
from _visualize import prettyPrintTree
from _type import TreeNode

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
                    T: type = int, NodeType: type = TreeNode, debug=False):
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
    def _deserializeBFS(cls, data, T: type=int, NodeType: type=TreeNode):
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
        # DONE: visualize tree
        print("visualize tree:")
        # prettyPrintTree(root, "????   ")
        prettyPrintTree(root, "")

# Your Codec object will be instantiated and called as such:
def test():
    codec = Codec()

    root = codec.deserialize("[]", debug=True)
    assert codec.serialize(root, debug=True) == "[]"

    assert codec.serialize(codec.deserialize("[1,2]", debug=True), debug=True) == "[1,2]"
    assert codec.serialize(codec.deserialize("[1,2,3]", debug=True), debug=True) == "[1,2,3]"

    root = codec.deserialize("[1, 2, 3, null,null,4,5]", debug=True)
    assert codec.serialize(root, debug=True) == "[1,2,3,null,null,4,5]"

    root = codec.deserialize("[null,2,3,null,null,4,5]", debug=True)
    assert codec.serialize(root, debug=True) == "[]"

    testCases = [
        "[]",
        "[1]",
        "[1,null,2,null,3,null,4,null,5]",
        "[1,6,2,7,null,null,3,null,null,null,4,6,5]",
        "[1,null,2,3,null,null,4,5]",
        '[3,5,1,6,2,0,8,null,null,7,4]',
    ]

    print('================================================================================')
    print('\ntest tree visualization:\n')
    root = Codec.deserialize("[]", int, debug=True)
    root = Codec.deserialize("[1]", int, debug=True)
    root = Codec.deserialize("[1,null,2,null,3,null,4,null,5]", int, debug=True)
    root = Codec.deserialize("[1,6,2,7,null,null,3,null,null,null,4,6,5]", int, debug=True)
    # root = Codec.deserialize("[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]", int, debug=True)
    root = Codec.deserialize(
        "[{}]".format(','.join(str(x) for x in range(1,50))), int, debug=True)
    root = codec.deserialize("[1,null,2,3,null,null,4,5]", debug=True)
    root = Codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]', int, debug=True)

    print('self test passed')


if __name__ == '__main__':
    test()
