#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
199. Binary Tree Right Side View Add to List

Total Accepted: 70063
Total Submissions: 178731
Difficulty: Medium
Contributors: Admin

Given a binary tree, imagine yourself standing on the right side of it, return the
values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

==============================================================================================
SOLUTION

1. Breadth-first search
Complexity: O(n), O(n)

2. Depth-first search
Modified preorder traversal: root, right child, left child

Complexity: O(n), O(logN)

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # return self.rightSideViewBFS(root)
        return self.rightSideViewDFS(root)

    def rightSideViewBFS(self, root):
        result = []
        frontier = root and [root]
        frontier_new = []
        while frontier:
            result.append(frontier[-1].val)
            while frontier:
                node = frontier.pop(0)
                for child in (node.left, node.right):
                    if child:
                        frontier_new.append(child)
            frontier, frontier_new = frontier_new, frontier
            frontier_new.clear()
        # print(result)
        return result

    def rightSideViewDFS(self, root):
        def dfs(node, depth):
            if not node:
                return
            if len(result) <= depth:
                result.append(node.val)
            if node.right: dfs(node.right, depth + 1)
            if node.left: dfs(node.left, depth + 1)

        result = []
        dfs(root, 0)
        return result

def test():
    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.rightSideView(root) == []

    root = Codec.deserialize("[1]", int)
    assert solution.rightSideView(root) == [1]

    root = Codec.deserialize("[1,2,3,null,5,null,4]", int)
    assert solution.rightSideView(root) == [1, 3, 4]

    root = Codec.deserialize("[1,2,3,null,5]", int)
    assert solution.rightSideView(root) == [1, 3, 5]

    print('self test passed')

if __name__ == '__main__':
    test()
