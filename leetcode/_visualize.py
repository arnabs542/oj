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
    '''
    if not node:
        print("<Empty tree>")
        return

    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft is True else "    "), False)

    print(prefix + ("    " if isLeft is None else ("└── " if isLeft else "┌── ")) + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("│   " if isLeft is False else "    "), True)
