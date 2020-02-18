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

A binary search tree produces ordered sequence when traversed in-order.
How to recover a increasingly sorted array if two numbers are swapped?
Input:   [1,2,3,4,5,6]
Swapped: [1,2,4,3,5,6], swap 4, 3
Swapped: [1,5,3,4,2,6], swap 5, 2
Swapped: [4,2,3,1,5,6], swap 1, 1

Since the array is INCREASING, except two numbers are swapped, if we scan
the array from left to right, we will find violations:
    current value smaller than previous one.
Where is the right number that's swapped? Just before first violation!
Where is the left number that's swapped? It could be the first violation, or
it could be the second violation!

1. recursive?

2. inorder traversal to find first peak(local maximum) and last valley(local minimum)?

3. morris traversal?

FOLLOW UP
================================================================================

1. Sort an almost sorted array where only two elements are swapped.
https://www.geeksforgeeks.org/sort-an-almost-sorted-array-where-only-two-elements-are-swapped/

Inspect what the array looks like when we swap two elements of a ascending
sorted array.
Suppose the swapped pair is (i, j) where i < j.
1) We need to find the left larger number at position i(nums[i] = nums0[j]).
And this number i: nums[i] > nums[i-1] and nums[i] > nums[i+1], which can be
simplified to nums[i] > nums[i+1].
2) Find the right smaller number at j (nums[j] = nums0[i]).
Such j has property: nums[j] < nums[j-1] and nums[j] < nums[j+1], which can be
simplified to nums[j] < nums[j-1].
Remember there will be two such j if i and j are not adjacent to each other.
In such case, choose last j.


'''

from _tree import Codec, TreeNode

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
        self.recoverTreeInorderSuccessor(root)
        # self.recorverTreeRecursive(root)
        # self.recorverTreeStackFrame(root)

        return root

    def recorverTreeRecursive(self, root):
        # recursive implementation(figure out recurrent relation first!)
        pair = [None, None]
        def dfs(prev, node):
            if node.left: # visit left
                prev = dfs(prev, node.left)
            if prev and prev.val > node.val: # visit current
                pair[0] = pair[0] or prev
                pair[1] = node # TODO: early stop
            prev = node
            if node.right: # visit right
                prev = dfs(prev, node.right)

            return prev # previous node for next successor

        if root: dfs(None, root) # maintain: prev, current. return last node
        if pair[0] and pair[1]:
            pair[0].val, pair[1].val = pair[1].val, pair[0].val

    def recorverTreeStackFrame(self, root):
        pair = [None, None]
        stack = [(None, root, 0)] if root else [] # prev, node, return address
        prev = None
        ret = None # corresponding return value of recursive procedure call
        while stack:
            prev, node, address = stack.pop()
            if address == 0:
                stack.append((prev, node, address+1))
                if node.left: stack.append((prev, node.left, 0))
                else: ret = None # reset return value
            elif address == 1: # this branch is triggered with NULL node.left from above
                prev = ret or prev
                if prev and prev.val > node.val:
                    pair[0] = pair[0] or prev
                    pair[1] = node # TODO: early stop
                prev = node
                stack.append((prev, node, address+1))
                if node.right: stack.append((node, node.right, 0))
                else: ret = None
            else:
                ret = ret or prev # XXX

        if pair[0] and pair[1]:
            pair[0].val, pair[1].val = pair[1].val, pair[0].val

    def recoverTreeInorderSuccessor(self, root: TreeNode):
        prev = None
        peak, valley = None, None
        stack = [root] if root else []
        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(node.left) # successor: push NULL left child as trigger for stack pop
            elif stack:
                node = stack.pop()
                stack.append(node.right)
                # prev, curr = curr, node
                # check violation of increasing order
                if prev and prev.val > node.val: # violation of order
                    peak, valley = peak or prev, node # at most two violation!
                prev = node
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

    root = Codec.deserialize('[1,2,#,3,#,0,#]', int)
    # assert Codec.serialize(solution.recoverTree(root)) == '[0,1,2,3]'

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
