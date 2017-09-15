#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _dataStructure import ListNode

def linkedList(l):
    if not l:
        return None
    head = ListNode(l[0])
    p = head
    for i in range(1, len(l)):
        node = ListNode(l[i])
        p.next = node
        p = node

    return head

def tolist(head, until=None):
    p = head
    result = []
    while p not in (None, until):
        result.append(p.val)
        p = p.next
    return result

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    result, frontier, frontier_new = [], [root] if root else [], []
    while frontier:
        result.append([])
        while frontier:
            node = frontier.pop(0)
            print(node)
            result[-1].append(node.val)
            for child in (node.left, node.right):
                if child: frontier_new.append(child)
        frontier_new, frontier = frontier, frontier_new
    # print(result)
    return result
