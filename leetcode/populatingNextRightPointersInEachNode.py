#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
116. Populating Next Right Pointers in Each Node

Total Accepted: 120047
Total Submissions: 325339
Difficulty: Medium
Contributors: Admin
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and
every parent has two children).

For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

==============================================================================================
SOLUTION

1. Breadth-first search
This method requires auxiliary space to store search frontiers.

2. Depth-first search

Observation:
1. A node's directly connected children(siblings) are very easy to connect:
    node.left.next = node.right
2. The problem occurs when connecting cousins, where we have to keep track of the previous
3. The previous node between cousins are always on the right branch.

Eliminate the O(N/2) auxiliary space, using O(logn) in function call stack actually.

3. Simultaneously construct the next pointer and do BREADTH-FIRST SEARCH.
Because we build up the next pointers on the fly, the nodes on higher layers, are already
connected properly. Then we don't need a list as the search frontier, because the next pointer
of parent will lead us to the next node on the same level!

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
        # return self.connectDFS(root)
        return self.connectBFS(root)

    def connectDFS(self, root):
        def dfs(node, previous):
            if not node:
                return
            if node.left:
                node.left.next = node.right
            if previous:
                # while previous.next:
                    # previous = previous.next
                previous.next = node.left

            previous = dfs(node.left, previous and previous.right)
            previous = dfs(node.right, previous)
            return node.right  # return node.right as the previous pointer
        dfs(root, None)

    def connectBFS(self, root):
        # TODO(done): breadth-first search
        head = root
        while head:
            node = head
            while node:
                if node.left:
                    node.left.next = node.right
                    node.right.next = node.next and node.next.left
                node = node.next
            head = head.left

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

    print("self test passed")

if __name__ == '__main__':
    test()
