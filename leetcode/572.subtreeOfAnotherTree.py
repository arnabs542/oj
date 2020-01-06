#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
572. Subtree of Another Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.

================================================================================
SOLUTION

1. Brute force
For each subtree of s, compare whether it's identical to tree t.

Complexity: O(mn), O(max(m, n))

2. Traverse and find substring

Note that when traversing, the NULL nodes must be explicitly kept to represent the tree structure.

1) Rather than assuming a null value for the childern of the leaf nodes, we need to treat the
left and right child as a lnull and rnull value respectively. To avoid substring match ambiguity.

2) Adding a '#' before every considering every value. If this isn't done, the trees of the form
s:[23, 4, 5] and t:[3, 4, 5] will also give a true result since the preorder string of the
t("23 4 lnull rull 5 lnull rnull") will be a substring of the preorder string of
s("3 4 lnull rull 5 lnull rnull"). Adding a '#' before the node's value solves this problem.

Complexity: O(mn), O(max(m, n))

"""

from _type import TreeNode
from serializeAndDeserializeBinaryTree import Codec

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        result = self._isSubtreeBruteForce(s, t)

        print(result)

        return result

    def _isSubtreeBruteForce(self, s: TreeNode, t: TreeNode):
        def identical(p, q):
            if not (p and q):
                return not (p or q)
            if p.val != q.val:
                return False
            if not identical(p.left, q.left):
                return False
            if not identical(p.right, q.right):
                return False
            return True

        def dfs(p: TreeNode):
            '''
            Identical or not
            '''
            if identical(p, t): return True
            if not p: return False
            return dfs(p.left) or dfs(p.right)
        return dfs(s)

    # TODO: traverse and use substring algorithm?


def test():

    solution = Solution()

    s = Codec.deserialize("[]")
    t = Codec.deserialize("[]")
    assert solution.isSubtree(s, t)

    s = Codec.deserialize("[1]")
    t = Codec.deserialize("[]")
    assert solution.isSubtree(s, t)

    s = Codec.deserialize("[]")
    t = Codec.deserialize("[1]")
    assert not solution.isSubtree(s, t)

    s = Codec.deserialize("[3,4,5,1,2]")
    t = Codec.deserialize("[4,1,2]")
    assert solution.isSubtree(s, t)

    s = Codec.deserialize("[3,4,5,1,2,null,null,0]")
    t = Codec.deserialize("[4,1,2]")
    assert not solution.isSubtree(s, t)

    print("self test passed")

if __name__ == '__main__':
    test()
