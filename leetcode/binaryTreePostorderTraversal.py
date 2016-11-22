#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
145. Binary Tree Postorder Traversal

Total Accepted: 119510
Total Submissions: 315369
Difficulty: Hard
Contributors: Admin

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a  binary tree node
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        pass

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # return self.postorderTraversalRecursive(root)
        return self.postorderTraversalStack(root)

    def postorderTraversalRecursive(self, root, visit=None):
        if visit is None: visit = []
        if root is not None:
            self.postorderTraversalRecursive(root.left, visit)
            self.postorderTraversalRecursive(root.right, visit)
            visit.append(root.val)
        return visit

    def postorderTraversalStack(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        vertices = []
        stack = [root] if root else []
        while stack:
            vertex = stack[-1]
            # XXX: PUSH frontiers
            for neighbor in (vertex.right, vertex.left):
                if neighbor: stack.append(neighbor)
            if not (vertex.left or vertex.right):
                vertices.append(vertex.val)
                stack.pop()
                # XXX: POP for dead end(no more neighbors), stack top is gray vertex(
                # neighbors are being explored)
                while stack and vertex in (stack[-1].left, stack[-1].right):
                    vertex = stack.pop()
                    vertices.append(vertex.val)

        print(vertices)
        return vertices

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.postorderTraversal(root) == []

    root = Codec.deserialize("[-3]", int)
    assert solution.postorderTraversal(root) == [-3]

    root = Codec.deserialize("[1,null,2,3]", int)
    assert solution.postorderTraversal(root) == [3, 2, 1]

    root = Codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]', int)
    assert solution.postorderTraversal(root)

    print('self test passed')

if __name__ == '__main__':
    test()
