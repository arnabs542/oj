#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
236. Lowest Common Ancestor of a Binary Tree

Total Accepted: 69900
Total Submissions: 239258
Difficulty: Medium
Contributors: Admin

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes v and w as the lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA
of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
===============================================================================================
SOLUTION:
    1. parent pointer from children nodes
    2. recursively traverse the root of the binary search tree.
        2.1 store paths to nodes
        2.2 with a single traversal
        2.3 range minimum query

2.1 is straightforward.

2.2, A common ancestor is the node that has all of the nodes as descendants, on the left or right.
So if we find a given descendant on the left, and another given descendant on the right, then the
current root node is the lowest common ancestor(and its ancestors are common ancestors but not
lowest).

2.3 Refer to geeksforgeeks(http://www.geeksforgeeks.org/find-lca-in-binary-tree-using-rmq/).
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution(object):

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        lca = self.lowestCommonAncestorDFS(root, p, q)
        print('lca of {} and {} is {}'.format(p, q, lca.val))
        return lca

    def lowestCommonAncestorStorePath(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # TODO: find lowest common ancestor by comparing paths

    def lowestCommonAncestorDFS(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        Recursively traverse the tree, determine whether a node is a common ancestor by
        check its descendants' existence.
        """
        # XXX: find lowest common ancestor with a single traversal utilizing common
        # ancestor's properties w.r.t descendant
        if root in (None, p, q) or root.val in (p, q):
            return root
        leftlca = self.lowestCommonAncestorDFS(root.left, p, q)
        rightlca = self.lowestCommonAncestorDFS(root.right, p, q)
        return root if leftlca and rightlca else leftlca or rightlca

    def lowestCommonAncestorRMQ(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode

        Reduce the lowest common ancestor problem to a range minimum query problem by
        traversal of the root by an Euler tour(traversal without lifting pencil), which
        is a depth-first search traversal with a preorder characteristics.
        """
        # TODO: range minimum query solution to lowest common ancestor

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize('[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]', int)
    print('tree is ', Codec.serialize(root))

    assert solution.lowestCommonAncestor(root, 5, 1).val == 3
    assert solution.lowestCommonAncestor(root, 5, 4).val == 5
    assert solution.lowestCommonAncestor(root, 7, 4).val == 2
    assert solution.lowestCommonAncestor(root, 2, 8).val == 3

    print('self test passed')

test()
