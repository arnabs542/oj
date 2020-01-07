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

    def hasNext(self):
        """
        :rtype: bool
        """

    def next(self):
        """
        :rtype: int
        """

class BSTIteratorStackFrame(object):

    def __init__(self, root: TreeNode):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = [(root, 0)] if root else []
        self.queue = []
        self._successor()

    def _successor(self):
        stack = self.stack
        while stack:
            v, address = stack.pop()
            if not v: continue
            if address == 0:
                stack.append((v, address + 1)) # keep pushing stack and update return address
                if v.left: stack.append((v.left, 0)) # stop pushing for NULL left child
            elif address == 1: # found NULL left child, visit
                self.queue.append(v)
                if v.right: stack.append((v.right, 0))
                break # XXX: to implement a iterator is to add a break point before every visit

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue or self.stack

    def next(self):
        """
        :rtype: int
        """
        # vertex = self.stack.pop()
        val = self.queue.pop(0).val
        self._successor()

        return val


class BSTIteratorStackFrameSimplified(object):

    def __init__(self, root: TreeNode):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        self._successor(self.root)

    def _successor(self, root):
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
        self._successor(vertex.right)

        return val

def test():

    from _tree import Codec

    # BSTIterator = BSTIteratorStackFrame
    BSTIterator = BSTIteratorStackFrameSimplified

    # Your BSTIterator will be called like this:
    root = Codec.deserialize("[]", int)
    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    assert v == []

    root = Codec.deserialize("[3,2,4,1]", int)
    i, v = BSTIterator(root), []
    while i.hasNext():
        v.append(i.next())
    assert v == [1, 2, 3, 4], print(v)

    root = Codec.deserialize("[1,null,2]", int)
    i, v = BSTIterator(root), []
    while i.hasNext(): v.append(i.next())
    assert v == [1, 2]

    print('self test passed')

if __name__ == '__main__':
    test()
