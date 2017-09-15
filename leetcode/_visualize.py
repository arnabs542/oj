#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _dataStructure import TreeNode

def prettyPrintTree(node: TreeNode, prefix="", isLeft=True):
    '''
    Pretty print tree

    This is a reverse inorder traversal procedure:
        visit right child, root node, left child
    '''
    if not node:
        print("<Empty tree>")
        return
    if node.right:
        prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)
