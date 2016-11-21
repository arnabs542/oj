#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
25. Reverse Nodes in k-Group

Total Accepted: 75971
Total Submissions: 258470
Difficulty: Hard
Contributors: Admin

Given a linked list, reverse the nodes of a linked list k at a time and return its
modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should
remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

==============================================================================================
SOLUTION:
    1. dummy pointer
    2. Maintain the SPLIT POINTER, then reverse the linked list nodes group by group
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        split = dummy
        while True:
            p = split
            # validation
            for _ in range(k):
                p = p.next
                if not p:
                    return dummy.next

            # the reversing part
            prev, p = split.next, split.next.next
            for _ in range(k - 1):
                prev.next = p.next
                p.next = split.next
                split.next = p
                p = prev.next

            split = prev

        return dummy.next

def test():
    from utils import linkedList, tolist
    solution = Solution()

    l = []
    head = linkedList(l)
    head_new = solution.reverseKGroup(head, 2)
    l_new = tolist(head_new)
    assert l_new == []

    l = [1]
    head = linkedList(l)
    head_new = solution.reverseKGroup(head, 2)
    l_new = tolist(head_new)
    assert l_new == [1]

    l = [1, 2, 3, 4, 5]
    head = linkedList(l)
    head_new = solution.reverseKGroup(head, 2)
    l_new = tolist(head_new)
    assert l_new == [2, 1, 4, 3, 5]

    l = [1, 2, 3, 4, 5]
    head = linkedList(l)
    head_new = solution.reverseKGroup(head, 3)
    l_new = tolist(head_new)
    assert l_new == [3, 2, 1, 4, 5]

    print('self test passed')

if __name__ == '__main__':
    test()
