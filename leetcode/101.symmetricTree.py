#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
101. Symmetric Tree

Total Accepted: 159571
Total Submissions: 425580
Difficulty: Easy
Contributors: Admin

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

==============================================================================================
SOLUTION

1. Inorder traversal, check palindrome (WON'T WORK)
This method suffers from incomplete binary tree, where it won't  be able to differentiate.
Such as the following tree:
    1
   / \
  2   3
 /   /
3   2

2. Breadth-first search
Keep track of corresponding nodes, including NULL, on each level, and check palindrome.

3. Recursive two subtree's symmetry
A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
Two trees are a mirror reflection of each other if:
    1) Their two roots have the same value.
    2) The right subtree of each tree is a mirror reflection of the left subtree of the other tree.

Then we can ship the recurrence relation solution.

Complexity: O(n), O(h), where h is bound by the height of tree.

4. Recursive two subtree's symmetry

5. Optimize space?

'''

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # return self.isSymmetricInorder(root)
        # return self.isSymmetricRecursive(root)
        return self.isSymmetricIteratively(root)

    def isSymmetricInorder(self, root):
        # FIXME: deal with incomplete binary tree
        def dfs(node):
            if not node:
                # result.append(-1)
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        result = []
        dfs(root)
        print(result)
        return result == list(reversed(result))

    def isSymmetricRecursive(self, root):
        def isMirror(p, q):
            if not (p and q):
                return p == q
            return p.val == q.val and isMirror(
                p.left, q.right) and isMirror(p.right, q.left)
        return not root or isMirror(root.left, root.right)

    def isSymmetricIteratively(self, root):
        # DONE: Iterative implementation of checking mirror reflection
        stack = [(root.left, root.right)] if root else []
        while stack:
            p, q = stack.pop()
            if not (p and q):
                if p != q:
                    return False
                else:
                    continue
            if p.val != q.val:
                return False
            stack.append((p.left, q.right))
            stack.append((p.right, q.left))
        return True

def test():
    from serializeAndDeserializeBinaryTree import Codec
    solution = Solution()

    root = Codec.deserialize('[]', int)
    assert solution.isSymmetric(root)

    root = Codec.deserialize('[1]', int)
    assert solution.isSymmetric(root)

    root = Codec.deserialize('[1,2,2,3,4,4,3]', int)
    assert solution.isSymmetric(root)

    root = Codec.deserialize('[1,2,2,3,null,null,3]', int)
    assert solution.isSymmetric(root)

    root = Codec.deserialize('[1,2,2,null,3,null,3]', int)
    assert not solution.isSymmetric(root)

    root = Codec.deserialize('[1,2,3,3,null,2,null]', int)
    assert not solution.isSymmetric(root)

    print("self test passed")

if __name__ == '__main__':
    test()
