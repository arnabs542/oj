#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
26. Largest BST Subtree

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST),
where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:

    10
    / \
   5  15
  / \   \
 1   8   7
The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.



Hint:

    You can recursively use algorithm similar to 98. Validate Binary Search Tree at each
node of the tree, which will result in O(nlogn) time complexity.

Follow up:
    Can you figure out ways to solve it with O(n) time complexity?

================================================================================
SOLUTION

1. Brute force verify
Complexity: O(nlogn), worst case is O(n²) for skewed tree.

2. Recurrence relation

A tree is BST only if its left right subtrees are also BST, and within
proper range defined by BST property.

Define state as a tuple of:
    (
    largest BST size so far,
    current tree is BST,
    current BST subtree value range,
    )

Then we can have state transition.

largest size so far = max(
  largest size so far on left,
  largest size so far on right,
  current subtree size if current is binary search tree too
)

Complexity: O(N)

'''


# TODO: implementation

class Solution:

    pass

def test():
    solution = Solution()

    print("self test passed")

if __name__ == '__main__':
    test()

