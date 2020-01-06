#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
538. Convert BST to Greater Tree

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

==============================================================================================
SOLUTION

A tree problem, illustrates graph structure and has recursive structure.
Consider recursive solution.

1. Depth first search
Greater than relation has dependency on its right children, which is a topological sort
problem in graph theory.

This is actually a special dfs(reverse in-order traversal): right child, root, left child.

Define the state we're tracking:
    f(node) = prefix sum so far, during the traversal of tree.

    f(node) = f(parent) + f(node.right), where parent is the lowest node with node in
the left child subtree.

Complexity: O(N), O(N)

2. Iterative solution

Complexity: O(N), O(N)

3. Reverse Morris In-order Traversal

Complexity: O(N), O(1)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        result = self._convertBSTDfs(root)

        return result

    def _convertBSTDfs(self, root):
        def dfs(node, prefixSum):
            """
            parent sum,
            right sum,
            current node value,
            """
            if not node: return prefixSum
            prefixSum = dfs(node.right, prefixSum)

            prefixSum += node.val
            node.val = prefixSum

            prefixSum = dfs(node.left, prefixSum)

            return prefixSum

        dfs(root, 0)

        return root

    # TODO: iterative solution
    # TODO: Morris in-order traversal

def test():
    solution = Solution()

    from serializeAndDeserializeBinaryTree import Codec

    root = Codec.deserialize("[]", int)
    assert Codec.serialize(solution.convertBST(root), debug=True) == "[]"

    root = Codec.deserialize("[1]", int)
    assert Codec.serialize(solution.convertBST(root), debug=True) == "[1]"

    root = Codec.deserialize("[5,1]", int)
    assert Codec.serialize(solution.convertBST(root), debug=True) == "[5,6]"

    root = Codec.deserialize("[5,1,9]", int)
    assert Codec.serialize(solution.convertBST(root), debug=True) == "[14,15,9]"

    root = Codec.deserialize("[5,2,13]", int)
    assert Codec.serialize(solution.convertBST(root), debug=True) == "[18,20,13]"

    print("self test passed!")

if __name__ == "__main__":
    test()
