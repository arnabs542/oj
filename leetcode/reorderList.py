#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
143. Reorder List Add to List

Total Accepted: 85914
Total Submissions: 345322
Difficulty: Medium
Contributors: Admin
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

==============================================================================================
SOLUTION

1. Reverse rear half and merge

'''

from _utils import *

# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.next = None

class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        self.reorderListReverseAndMerge(head)

    def reorderListReverseAndMerge(self, head):
        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next and fast.next.next

        front = ListNode(0)
        front.next = None
        p = slow.next
        slow.next = None

        # reverse
        while p:
            q = p.next
            p.next = front.next
            front.next = p
            p = q

        # merge
        p, q = dummy.next, front.next
        while p and q:
            q1 = q.next
            q.next = p.next
            p.next = q
            p, q = q.next, q1

def test():
    solution = Solution()

    l = linkedList([])
    solution.reorderList(l)
    print(tolist(l))
    assert tolist(l) == []

    l = linkedList([1, 2, 3, 4])
    solution.reorderList(l)
    print(tolist(l))
    assert tolist(l) == [1, 4, 2, 3]

    l = linkedList([1, 2, 3, 4, 5])
    solution.reorderList(l)
    print(tolist(l))
    assert tolist(l) == [1, 5, 2, 4, 3]

    l = linkedList([1, 2, 3, 4, 5, 6, 7, 8])
    solution.reorderList(l)
    print(tolist(l))
    assert tolist(l) == [1, 8, 2, 7, 3, 6, 4, 5]

    print("self test passed")

if __name__ == '__main__':
    test()
