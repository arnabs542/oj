#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _dataStructure import TreeNode

def prettyPrintTree(node: TreeNode, prefix="", isLeft=None):
    '''
    Pretty print tree

    This is a reverse inorder traversal procedure:
        visit right child, root node, left child

    The whole point of visualizing a tree is to spare room for later nodes to be visited.

    A vertical '|' should be placed where the drawing expands from inside to outside:
        right child of left parent, or left child right parent.

    Used symbols: "┌", "─", "└", "│"
    ------------------------------------------------------------------------------------------
    SOLUTION
    The basic idea is tree traversal. Different traversal methods can produce different
    ASCII visualization of tree structure.

    And the only varying variables are: horizontal and vertical indentation.
    This method will traverse the tree in a preorder approach. So, we need to expand space for
    in-going nodes: right child of left parent or vice versa.


    -----------------------------------------------------------------------------------------
    Example

                ┌── 31
            ┌── 15
            │   └── 30
        ┌── 7
        │   │   ┌── 29
        │   └── 14
        │       └── 28
    ┌── 3
        │       ┌── 27
        │   ┌── 13
        │   │   └── 26
        └── 6
            │   ┌── 25
            └── 12
                │   ┌── 49
                └── 24
                    └── 48

    '''
    if not node:
        print("<Empty tree>")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft is True else "    "), False)

    print(prefix + ("    " if isLeft is None else ("└── " if isLeft else "┌── ")) + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("│   " if isLeft is False else "    "), True)
