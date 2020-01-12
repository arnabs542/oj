#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
124. Binary Tree Maximum Path Sum

Total Accepted: 80294
Total Submissions: 324647
Difficulty: Hard
Contributors: Admin

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any
node in the tree along the parent-child connections. The path must contain at least one node
and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.


================================================================================
SOLUTION

This is a longest path on an undirected acyclic graph(tree) problem.

Such a path starts from one node and ends at another node, so there are O(N²)
combinations. Given a tree, any two nodes have a COMMON ANCESTOR! And such path
must be connected through their common ancestor.
And such path can be DECOMPOSED of two simple paths starting with some node v,
each of which is a path from ancestor v to its some distant child(neighbor).

The problem STATE is composite, it would be easier to DECOMPOSE it into a tuple of
simpler ones with respect to a particular root node.
Define simple path as any path starting from a predecessor to a descendant node.

Simple STATE:
    (maximum left simple path sum ending here, maximum right simple path sum ending here)

1. Basic BRUTE-FORCE - enumerate all possible ancestors
    The start node could be any of all nodes.
    Traverse ALL THE NODES, and check their maximum sum left and right paths starting
there. This procedure involves repeated computation.

Check maximum sum of left and right paths takes average O(N). So the overall
time complexity is O(N²).

2. Depth first search - exhaust all ancestors with recurrence relation

So we can enumerate all possible ancestors and construct the target path
with some recurrence relation.

A path sum problem shares some similarity with maximum subarray problem, which both have
overlapping subproblems and optimal substructure. Parent vertices depend on its neighbors
(children). So there is a Dynamic Programming solution.

And the maximum path sum ending here depends on the maximum path sum ending with its direct
descendants.

--------------------------------------------------------------------------------
DEFINE STATE to contain enough information for RECURRENCE RELATION.
STATE AS TUPLE of (max_ending_here, max_so_far).

max_ending_here: the maximum sum of path from some distant neighbor(child) up to current node
max_so_far: maximum sum of two paths starting from/ending with current node to some two
distant neighbors.

For each vertex in the tree, there are two scenarios for max_ending_here state transition:
1. Current max path consists only one element at the position
2. Current maximum path consists of one more element than the previous maximum path.

Then we have RECURRENCE RELATION to its neighbors(children). And the STATE contains full
information for different scenarios in the recurrence relation, so repeated calculations
can be spared.

Move STATE via RETURN VALUE to solve the overlapping optimal substructure in a BOTTOM-UP/
BACKWARD manner.

################################################################################
FOLLOW UP

1. Find the maximum path distance(543. Diameter of Binary Tree)

WARN
Define state: (max_distance_ending_here, max_distance_so_far) will be bad!
This is because nodes path [] and [1] both have same value distance of 0, but the
state transition will give totally different next state 0 and 1. Then the recurrence relation
will lose information because of incorrect mapping!

Instead, define tractable state as a tuple:
    (globally optimal: max_distance_so_far, maximum number of nodes of paths)

Note that if a node's child is empty, the distance increase from the child subtree should be 0!

2. Find the maximum distance paths
Define state: (max_distance_path_ending_here, max_distance_path_so_far)
State is a tuple of list, representing path sequence.

3. With negative numbers?
Maximum subarray on tree data structure, already covered by this solution.

4. Maximum sum sequence?
Just add non-negative numbers

5. Binary tree maximum path product

'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = self._maxPathSumRecursion(root)

        print("result: ", result)

        return result

    def _maxPathSumRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Returns
        -------
        A state of tuple: (max_ending_here, max_so_far)
        """
        def dfs(node):
            if not node:
                return 0, float('-inf')
            left, right = dfs(node.left), dfs(node.right)
            max_ending_here = max(left[0] + node.val, right[0] + node.val, node.val)
            max_so_far = max(max_ending_here, left[1], right[1], left[0] + right[0] + node.val,)
            # print(node, max_ending_here, max_so_far)
            return max_ending_here, max_so_far

        t = dfs(root) if root else (0, 0)
        print(t, '\n')
        return t[1]

    def _maxPathSum2Recursion(self, root):
        """
        :type root: TreeNode
        :rtype: int

        For follow-up problem where a path is defined as a sequence of nodes starting
        from some node down to some children via parent-child connections
        """
        def dfs(node):
            if not node:
                return 0, float('-inf')
            left, right = dfs(node.left), dfs(node.right)
            max_ending_here = max(left[0] + node.val,
                                  right[0] + node.val,
                                  left[0] + right[0] + node.val,
                                  node.val
                                 )
            max_so_far = max(left[1], right[1], max_ending_here)
            print(node, max_ending_here, max_so_far)
            return max_ending_here, max_so_far



def test():

    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.maxPathSum(root) == 0

    root = Codec.deserialize("[-3]", int)
    assert solution.maxPathSum(root) == -3

    root = Codec.deserialize("[1,2,3]", int)
    assert solution.maxPathSum(root) == 6

    root = Codec.deserialize('[3,5,1,6,2,0,8,null,null,7,4]', int)
    assert solution.maxPathSum(root) == 26

    root = Codec.deserialize('[3,5,1,6,2,0,8,null,null,-7,4]', int)
    assert solution.maxPathSum(root) == 23

    root = Codec.deserialize('[1, 2, 3,null, null, -4, 5]', int)
    assert solution.maxPathSum(root) == 11

    print('self test passed')

if __name__ == '__main__':
    test()
