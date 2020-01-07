#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
437. Path Sum III

Total Accepted: 6546
Total Submissions: 17133
Difficulty: Easy
Contributors: Stomach_ache

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

================================================================================
SOLUTION

1. Brute force - recursion - depth first search

A path contains two ends, and has O(N²) combinations. One path can at start any
node, so we exhaust all possible paths.

Complexity: O(N²)

2. Recursion with prefix sum

With prefix sum hash table, we can count number of paths ending with current node
summing up to target in O(1).

Complexity: O(n)

################################################################################
FOLLOW UP
What if the path doesn't have to go downwards?
Then there are O(N²) different paths.

################################################################################
FOLLOW UP
Sequence sum?


'''

from _decorators import timeit

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    @timeit
    def pathSum(self, root: TreeNode, target: int):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        # result = self.pathSumRecursionUgly(root, target)
        result = self.pathSumRecursion(root, target)
        # result = self.pathSumRecursion2(root, target)
        # result = self.pathSumPrefixSum(root, target)

        print(result)

        return result

    def pathSumRecursion(self, root: TreeNode, target: int):
        def dfs(node, s, start=False):
            """
            Returns
            -------
            int: number of paths summing to target on this subtree.
            """
            if not node: return 0
            result = node.val == s
            result += dfs(node.left, s - node.val) + dfs(node.right, s - node.val) # following a path already started
            if start: result += dfs(node.left, target, start) + dfs(node.right, target, start) # start a new path here
            return result

        return dfs(root, target, True)

    def pathSumRecursion2(self, root: TreeNode, target: int, curr=None):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int

        Each time find all the path start from current node, O(logN) or O(N)
        Then move start node to the child and repeat the above procedure. (N nodes).
        Time Complexity should be O(N²) for the worst case and O(NlogN) for
        balanced binary Tree.
        """
        def findPath(root, target):
            '''
            return value in range (0, 1, 2, ...)
            '''
            result = 0
            if not root:
                return 0
            result += (target == root.val) + \
                    findPath(root.left, target - root.val) + \
                    findPath(root.right, target - root.val)
            return result

        if not root:
            return 0
        return findPath(root, target) + self.pathSumRecursion2(
            root.left, target) + self.pathSumRecursion2(root.right, target)

    def pathSumPrefixSum(self, root: TreeNode, target: int):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int

        Maintain a prefix sum list. Then if we want check subarray sum from i to j,
        we have: sum(i, j) = prefix[j] - prefix[i - 1].

        Here, we can use a hash table to store prefix sums, where key is the prefix sum and
        value is its number of occurrences.

        Then depth-first search and backtrack.

        Time Complexity is O(N), where N is the number of nodes in the tree.
        """
        # XXX: prefix sum solution
        def dfs(root, sum_so_far, target, prefix):
            """
            Traverse the binary tree and build up prefix sum hash table.
            """
            if not root:
                return 0
            # print('target', target, root, prefix)
            sum_so_far += root.val
            res = prefix.get(sum_so_far - target, 0) # number of subarrays summing to target

            prefix[sum_so_far] = prefix.get(sum_so_far, 0) + 1
            res += dfs(root.left, sum_so_far, target, prefix) + \
                dfs(root.right, sum_so_far, target, prefix)
            prefix[sum_so_far] -= 1  # backtrack: restore state to backtrack

            return res

        prefix = {0: 1} # XXX: initialize prefix sum with {0:1}
        return dfs(root, 0, target, prefix)

def test():

    from _tree import Codec

    solution = Solution()

    root = Codec.deserialize("[]", int)
    assert solution.pathSum(root, 1) == 0

    root = Codec.deserialize("[1,1,1]", int)
    assert solution.pathSum(root, 1) == 3

    root = Codec.deserialize('[1,null,2,null,3,null,4,null,5]', int)
    assert solution.pathSum(root, 3) == 2

    root = Codec.deserialize('[-8,null,8,null,2,null,-2]', int)
    assert solution.pathSum(root, -2) == 1

    root = Codec.deserialize('[-8,6,8,null,null,8,2,null,null,null,-2]', int)
    assert solution.pathSum(root, -2) == 2

    root = Codec.deserialize('[1,-2,-3,1,3,-2,null,-1]', int)
    assert solution.pathSum(root, -1) == 4

    root = Codec.deserialize("[5,3,2,3,-2,null,1]", int)
    assert solution.pathSum(root, 8) == 2

    root = Codec.deserialize("[10,5,-3,3,2,null,11,3,-2,null,1]", int)
    assert solution.pathSum(root, 8) == 3

    print('self test passed')
    pass

test()
