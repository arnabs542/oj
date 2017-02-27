#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
117. Populating Next Right Pointers in Each Node II

Total Accepted: 85862
Total Submissions: 255760
Difficulty: Medium
Contributors: Admin

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

==============================================================================================
SOLUTION

1. Same as the first problem, BFS on the fly!
But the tree may not be perfect or even complete, so we should be careful when updating
the head pointer, which points to the leftmost node on the next level.

'''

# Definition for binary tree with next pointer.
class TreeLinkNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return 'val = {}, next = {};'.format(
            self.val, self.next and self.next.val)

class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        self.connectBFS(root)

    def connectBFS(self, root: TreeLinkNode):
        head = root
        while head:
            node, left = head, None
            while node:
                # next head may not be the current head's left child
                if not (head.left or head.right) and (node.left or node.right):
                    head = node
                if left: left.next = node.left or node.right
                if node.left: node.left.next = node.right
                left = node.right or node.left or left
                node = node.next
            head = head.left or head.right

def test():
    from serializeAndDeserializeBinaryTree import Codec
    from utils import levelOrder

    solution = Solution()

    root = Codec.deserialize(str([]), int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize(str([1]), int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize(str([1, 2, 3]), int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize(str([1, 2, 3, 4, 5, 6, 7]), int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize('[1, 2, 3, 4, 5, null, 7]', int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize('[1, 2, 3, 4, null, null, 7]', int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize('[1, 2, 3, null, null, null, 7]', int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize('[1, 2, 3, 4, 5, null, 7, 8, 9, null, null, 14]', int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize('[1,2,3,4,5,null,null,null,null,10,null,11,12]', int, TreeLinkNode)
    solution.connect(root)
    levelOrder(root)
    print()

    root = Codec.deserialize('[-9,-3,2,#,4,4,0,-6,#,-5]', int, TreeLinkNode)
    print(Codec.serialize(root))
    solution.connect(root)
    levelOrder(root)
    # "{-9,#,-3,2,#,4,4,0,#,-6,-5,#}"
    print()


    print("self test passed")

if __name__ == '__main__':
    test()
