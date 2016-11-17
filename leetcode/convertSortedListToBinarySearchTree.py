#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
109. Convert Sorted List to Binary Search Tree

Total Accepted: 87956
Total Submissions: 271926
Difficulty: Medium
Contributors: Admin

Given a singly linked list where elements are sorted in ascending order, convert it to a
height balanced BST.

==============================================================================================
SOLUTION:
    Find the median element as the root of BST, then the left, right parts are left, right
children, which can be constructed with recursive call.
    Finding the median element could be achieved with FAST AND SLOW POINTER.
'''
# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def sortedListToBST(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        fast, slow = head, head
        left = None
        while fast and fast.next:
            fast = fast.next.next
            left, slow = slow, slow.next

        root = TreeNode(slow.val)
        if left:
            left.next = None
            root.left = self.sortedListToBST(head)

        right = slow.next
        root.right = self.sortedListToBST(right)

        return root
