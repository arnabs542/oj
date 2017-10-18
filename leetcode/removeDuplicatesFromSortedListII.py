#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
82. Remove Duplicates from Sorted List II

Total Accepted: 90886
Total Submissions: 320201
Difficulty: Medium
Contributors: Admin

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only
distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

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

        prev, curr = dummy, dummy.next
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next
            else:
                prev.next = curr.next
            curr = prev.next

        return dummy.next

def test():
    from _utils import linkedList, tolist
    solution = Solution()

    l = [1, 1, 2]
    head = linkedList(l)
    tolist(head)
    head_new = solution.deleteDuplicates(head)
    l_new = tolist(head_new)
    assert l_new == [2]

    l = [1, 1, 2, 3, 3]
    head = linkedList(l)
    tolist(head)
    head_new = solution.deleteDuplicates(head)
    l_new = tolist(head_new)
    assert l_new == [2]

    print('self test passed')

if __name__ == '__main__':
    test()
