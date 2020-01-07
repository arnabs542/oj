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

================================================================================
SOLUTION

1. Parent pointer from children nodes
Put v and all its ancestors in a hash set.
Exhaust w's ancestors, find the first that's in the hash set.

But, we don't have parent pointers.

Complexity: O(n), O(h)

2. Path prefix
Traverse the tree and store the paths to target nodes. Maintain a mapping between
the path's index to node.
Find the longest common prefix of the paths to nodes.

Auxiliary space: we need extra space to store the paths, and need to traverse
the tree in two passes.

Complexity: O(n), O(h), where n is the number of nodes in tree, and h is
the height of tree.

3. One pass traverse without extra space

How to infer the one pass solution without extra space?

Let's reduce it to a simple case, where we only need to find one node.
Now, in a depth first search manner, assume we found one target node p.

How do we go further?
We might want to search the subtree of p, if another target q is found,
then the lowest common ancestor of p and q is p.
What if q is not found is the subtree of p?
Then we might want to try siblings of p.
What if it's not found still?
Then try siblings of parents of p, backtracking recursively.

--------------------------------------------------------------------------------
Now it seems clear to define such state:
(
    node: found target node p or q, or the LCA of p and q
)
Call the recursive procedure, and return such state.

Then we can have state transition recurrence relation:
If neither p nor q is found, return null.
If either p or q is found, return the found target.
If both p and q is found, return the lowest node, where the lowest indicates
the deepest recursive node, where p and q is found within that subtree.

If we already found a match, we don't have to traverse any other nodes, so
we can add another state as return value, boolean match.

Takeaway
--------
A common ancestor is the node that has all of the nodes as descendants, on the left or right.
So if we find a given descendant on the left, and another given descendant on the right, then the
current root node is the lowest common ancestor(and its ancestors are common ancestors but not
lowest).

3 range minimum query
Refer to geeksforgeeks(http://www.geeksforgeeks.org/find-lca-in-binary-tree-using-rmq/).

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
        # lca = self._lowestCommonAncestorOnePass2(root, p, q)
        lca = self._lowestCommonAncestorOnePass(root, p, q)
        print('lca of {} and {} is {}'.format(p, q, lca.val))
        return lca

    def _lowestCommonAncestorStorePath(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # TODO: find lowest common ancestor by comparing paths

    def _lowestCommonAncestorOnePass(self, root: TreeNode, p: TreeNode, q: TreeNode):
        def dfs(node):
            if not node: return None, False
            # print(node.val, p, q)
            found = None
            if node in (p, q) or node.val in (p, q): found = node
            for child in (node.left, node.right):
                target, match = dfs(child)
                if match:
                    return target, match
                elif target == p or target and target.val == p:
                    if found == q or found and found.val == q: return node, True
                    found = target
                elif target == q or target and target.val == q:
                    if found == p or found and found.val == p: return node, True
                    found = target

            # print('found: ', found)
            return found, False
        return dfs(root)[0]

    def _lowestCommonAncestorOnePassOj(self, root: TreeNode, p: TreeNode, q: TreeNode):
        def dfs(node):
            if not node: return None, False
            found = None
            if node in (p, q): found = node
            for child in (node.left, node.right):
                target, match = dfs(child)
                if match: return target, match
                elif target == p:
                    if found == q: return node, True
                    found = target
                elif target == q:
                    if found == p: return node, True
                    found = target

            return found, False

        return dfs(root)[0]

    def _lowestCommonAncestorOnePass2(self, root: TreeNode, p: TreeNode, q: TreeNode):
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

    def _lowestCommonAncestorRMQ(self, root: TreeNode, p: TreeNode, q: TreeNode):
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

    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize('[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]', int)
    print('tree is ', Codec.serialize(root))

    assert solution.lowestCommonAncestor(root, 5, 1).val == 3
    assert solution.lowestCommonAncestor(root, 5, 4).val == 5
    assert solution.lowestCommonAncestor(root, 7, 4).val == 2
    assert solution.lowestCommonAncestor(root, 2, 8).val == 3

    print('self test passed')

test()
