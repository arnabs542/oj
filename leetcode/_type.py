#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return 'val = {}'.format(self.val)


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return '[{}, {}]'.format(self.start, self.end)
