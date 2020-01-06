#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
337. House Robber III

Total Accepted: 29368
Total Submissions: 71944
Difficulty: Medium
Contributors: Admin

The thief has found himself a new place for his thievery again. There is only one
entrance to this area, called the "root." Besides the root, each house has one and
only one parent house. After a tour, the smart thief realized that "all houses in
this place forms a binary tree". It will automatically contact the police if two
directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

==============================================================================================
SOLUTION:
    This problem has RECURRENCE RELATION between a vertex and its neighbors.
And inducing the problem backward, in a bottom-up fashion, could give very CLEAR STATE
TRANSITION formula.

For each vertex in the tree, there are two scenarios: it is robbed or not.

DEFINE STATE to contain enough information for recurrence relation:
    (maximum with robbing the current vertex, maximum without robbing the current vertex/node)

And the STATE contains full information for different scenarios in the RECURRENCE RELATION, so
repeated calculations can be spared.

To tackle BOTTOM-UP STATE TRANSITION problems with recursion, we could put out state at recursive
call's RETURN VALUE.
'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return self.robBFS(root)
        return self.robRecursion(root)

    def robBFS(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Dynamic programming with breadth-first search.
        Wrong recurrence relation:
            amount[depth] = max(amount[depth + 1], amount[depth + 2] + level_sum(depth))
        The recurrence relation is not about depth, but about directly parent-child
        connection.
        """
        # FIXME: wrong solution, doesn't deal with the 'directly-linked'
        # condition
        amount = []
        frontier, frontier_new = {root} if root else set(), set()
        while frontier:
            depth = len(amount)
            amount.append(0)
            level_sum = sum(map(lambda x: x.val, frontier))
            amount[depth] = max(
                amount[depth - 1] if depth else 0,
                (amount[depth - 2] if depth >= 2 else 0) + level_sum)
            # print('depth', depth, level_sum, amount)
            while frontier:
                vertex = frontier.pop()
                for child in (vertex.left, vertex.right):
                    if child:
                        frontier_new.add(child)
            frontier, frontier_new = frontier_new, frontier
            pass

        print(amount)
        return amount[-1] if amount else 0

    def robNaive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return max(val, self.robNaive(root.left), self.robNaive(root.right))

    def robRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: int

        """
        def dfs(root):
            if not root:
                return (0, 0)
            left, right = dfs(root.left), dfs(root.right)
            max_robbed = root.val + left[1] + right[1]
            max_not_robbed = max(left) + max(right)

            return max_robbed, max_not_robbed

        return max(dfs(root))

def test():

    from serializeAndDeserializeBinaryTree import Codec

    solution = Solution()

    root = Codec.deserialize("[3,2,3,null,3,null,1]", int)
    assert solution.rob(root) == 7

    root = Codec.deserialize('[3,4,5,1,3,null,1]', int)
    assert solution.rob(root) == 9

    root = Codec.deserialize('[2,1,3,null,4]', int)
    assert solution.rob(root) == 7

    print('self test passed')
    pass

if __name__ == '__main__':
    test()
