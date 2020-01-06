#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
99. Recover Binary Search Tree

Total Accepted: 63716
Total Submissions: 224220
Difficulty: Hard
Contributors: Admin

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

================================================================================
SOLUTION

MONOTONICITY analysis: the swapped nodes can be identified as first peak(local maximum)
and last valley(local minimum)

A binary search tree produces ordered sequence when traversed in-order.

1. recursive?

2. inorder traversal to find first peak(local maximum) and last valley(local minimum)?

3. Morris traversal?

'''

from serializeAndDeserializeBinaryTree import Codec, TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.recoverTreeInorder(root)
        return root
        # [nodes] = self.wrongNode(root)

    def recoverTreeInorder(self, root: TreeNode):
        prev, curr = None, None
        peak, valley = None, None
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(node.left)
            elif stack:
                node = stack.pop()
                stack.append(node.right)
                # check peak and valley
                prev, curr = curr, node
                if prev and prev.val > curr.val:
                    peak, valley = peak or prev, curr
        print(peak, valley)
        if peak and valley:
            peak.val, valley.val = valley.val, peak.val
        pass

def test():
    solution = Solution()

    root = Codec.deserialize('[]', int)
    assert Codec.serialize(solution.recoverTree(root)) == '[]'

    root = Codec.deserialize('[0,1]', int)
    assert Codec.serialize(solution.recoverTree(root)) == '[1,0]'

    # inorder: 1,2,3,4,5,6,7
    root = Codec.deserialize('[4,2,6,1,3,5,7]', int)
    assert Codec.serialize(solution.recoverTree(root)) == '[4,2,6,1,3,5,7]'

    # inorder: 1,2,5,4,3,6,7
    # 5, 4 → 5; 4, 3 → 3. Swap 4 and 3
    root = Codec.deserialize('[4,2,6,1,5,3,7]', int)
    assert Codec.serialize(solution.recoverTree(root)) == '[4,2,6,1,3,5,7]'

    # inorder: 2,1,3,4,5,6,7
    # 2, 1 → 2; swap 2 and 1
    root = Codec.deserialize('[4,2,6,1,5,3,7]', int)
    assert Codec.serialize(solution.recoverTree(root)) == '[4,2,6,1,3,5,7]'

    # inorder: 1,4,3,2,5,6,7
    # 4, 3 → 4, 3, 2 → 2, swap 4 and 2
    root = Codec.deserialize('[2,4,6,1,3,5,7]', int)
    assert Codec.serialize(solution.recoverTree(root)) == '[4,2,6,1,3,5,7]'

    print('self test passed')

if __name__ == '__main__':
    test()
    pass
