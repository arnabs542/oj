#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
606. Construct String from Binary Tree

Total Accepted: 5908
Total Submissions: 11052
Difficulty: Easy
Contributors:
love_Fawn
You need to construct a string consists of parenthesis and integers from a binary tree
with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit
all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between
the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, except we can't omit the first parenthesis
pair to break the one-to-one mapping relationship between the input and the output.

==============================================================================================
SOLUTION

Tree traversal problem(Graph problem).

Unnecessary parenthesis pairs are empty trailing subtree's deserialization.

1. Recursive solution

2. Stack: iterative solution

'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.tree2strRecursive(t)

    def tree2strRecursive(self, t):
        if not t:
            return ''
        root = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        return root + ('({})'.format(left) if (left or right)
                       else '') + ('({})'.format(right) if right else '')

    def tree2strIterative(self, t):
        # TODO: iterative traversal
        pass

def test():
    solution = Solution()

  # TODO: test those test cases
    # [1,2,3,4]
    # [1,2,3,null,4]
    # []
    # [1]
    # [1,2,null,3,null,4,null]

    print("self test passed")

if __name__ == '__main__':
    test()
