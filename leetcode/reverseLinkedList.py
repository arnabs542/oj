#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
206. Reverse Linked List

Total Accepted: 165411
Total Submissions: 385744
Difficulty: Easy
Contributors: Admin

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

==============================================================================================
SOLUTION:
    1. Iterative
    2. Recursive: bottom up return states

Approaches:
    1. reverse by swapping adjacent pointers
    2. reverse with First In Last Out order
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseListIterative(head)

    def reverseListIterative(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p, q = head, head.next
        head.next = None
        while p and q:
            r = q.next
            q.next = p
            p, q = q, r

        return p

    # TODO: use dummy variable and keep inserting new nodes directly after the dummy head

    def reverseListRecursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # TODO: recursion
