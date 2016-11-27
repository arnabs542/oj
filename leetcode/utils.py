#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

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