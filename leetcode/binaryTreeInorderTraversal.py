#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
94. Binary Tree Inorder Traversal

Total Accepted: 162943
Total Submissions: 377316
Difficulty: Medium
Contributors: Admin

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

==============================================================================================
SOLUTION:
    INORDER is different than PREORDER and POSTORDER in a way how we deal with GRAY VERTICES.
For inorder or postorder, just visit them before or after its descedants. The real trouble with
implementation is when to PUSH the right child. Immediately when the root is discovered or when
the POPPING and visiting the root vertex? Both will do, just difference ways.
'''

# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.visit = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # return self.inorderTraversalRecursive(root)
        # return self.inorderTraversalStack(root)
        return self.inorderTraversalStack2(root)

    def inorderTraversalRecursive(self, root):
        """
        :type root: treenode
        :rtype: list[int]
        """
        if root is not None:
            self.inorderTraversal(root.left)
            self.visit.append(root.val)
            self.inorderTraversal(root.right)
        return self.visit

    def inorderTraversalStack(self, root):
        """
        :type root: treenode
        :rtype: list[int]

        PUSH the right child when root is popped and visited.
        """
        vertices = []
        stack = [root] if root else []
        while stack:
            vertex = stack.pop()
            # XXX: avoid duplicate PUSHING the same node, giving infinite loop
            if vertex:
                stack.append(vertex)
                # PUSH left adjacent vertex
                stack.append(vertex.left)
            elif stack:
                # POP root vertex, because there is no left adjacent vertices anymore
                vertex = stack.pop()
                vertices.append(vertex.val)
                # XXX: and PUSH right vertices AFTER finishing EXPLORING ROOT
                stack.append(vertex.right)

        return vertices

    def inorderTraversalStack2(self, root):
        """
        :type root: treenode
        :rtype: list[int]

        PUSH the right child immediately when root is discovered.

        PUSH where we can, POP when there is no more to explore
        """
        vertices = []
        stack = [root] if root else []
        while stack:
            vertex = stack.pop()
            if vertex:
                stack.append(vertex.right)
                stack.append(vertex)
                # PUSH left adjacent vertex
                stack.append(vertex.left)
            elif stack:
                # POP root vertex, because there is no left adjacent vertices anymore
                vertex = stack.pop()
                vertices.append(vertex.val)

        return vertices

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.inorderTraversal(root) == []

    root = Codec.deserialize("[-3]", int)
    assert solution.inorderTraversal(root) == [-3]

    root = Codec.deserialize("[1,null,2,3]", int)
    assert solution.inorderTraversal(root) == [1, 3, 2]

    root = Codec.deserialize("[1,null,2,null,3,null,4,null,5]", int)
    assert solution.inorderTraversal(root) == [1, 2, 3, 4, 5]

    root = Codec.deserialize("[1,null,2,null,3,null,4,null,5]", int)
    assert solution.inorderTraversal(root) == [1, 2, 3, 4, 5]

    root = Codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]', int)
    assert solution.inorderTraversal(root) == [6, 5, 7, 2, 4, 3, 0, 1, 8]

    print('self test passed')

if __name__ == '__main__':
    test()
