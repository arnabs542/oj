#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
83. Remove Duplicates from Sorted List

Total Accepted: 150178
Total Submissions: 390104
Difficulty: Easy
Contributors: Admin

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

==============================================================================================
SOLUTION:
    TWO POINTER: previous node and current node.
    One tip: dummy head pointer.
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def deleteDuplicates(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        prev, p = dummy, dummy.next
        while p:
            if p.val == prev.val:
                prev.next = p.next
            else:
                prev = p

            p = prev.next

        return dummy.next

def test():
    from utils import linkedList, tolist
    solution = Solution()

    l = [1, 1, 2]
    head = linkedList(l)
    tolist(head)
    head_new = solution.deleteDuplicates(head)
    l_new = tolist(head_new)
    assert l_new == [1, 2]

    l = [1, 1, 2, 3, 3]
    head = linkedList(l)
    tolist(head)
    head_new = solution.deleteDuplicates(head)
    l_new = tolist(head_new)
    assert l_new == [1, 2, 3]

    print('self test passed')

if __name__ == '__main__':
    test()
