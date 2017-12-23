#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
173. Binary Search Tree Iterator

Total Accepted: 69522
Total Submissions: 181170
Difficulty: Medium
Contributors: Admin

Implement an iterator over a binary search tree (BST). Your iterator will be initialized
with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h
is the height of the tree.

==============================================================================================
SOLUTION:
    Binary search? Binary tree inorder traversal.
'''

# Definition for a  binary tree node
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root: TreeNode):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self._nextLeftLeaf(self.root)

    def _nextLeftLeaf(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        vertex = self.stack.pop()
        val = vertex.val
        self._nextLeftLeaf(vertex.right)

        return val

def test():

    from serializeAndDeserializeBinaryTree import Codec

    # Your BSTIterator will be called like this:
    root = Codec.deserialize("[]", int)
    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    assert v == []

    root = Codec.deserialize("[1,2,3,4]", int)
    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    assert v == [4, 2, 1, 3]

    root = Codec.deserialize("[1,null,2]", int)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    assert v == [1, 2]

    print('self test passed')

if __name__ == '__main__':
    test()
