#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
21. Merge Two Sorted Lists Add to List

Total Accepted: 199353
Total Submissions: 520026
Difficulty: Easy
Contributors: Admin

Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.

==============================================================================================
SOLUTION

1. Dummy head, keep track of the new tail, append the smaller one.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.mergeTwoLists1(l1, l2)

    def mergeTwoLists1(self, l1, l2):
        tail = dummy = ListNode(0)
        while l1 or l2:
            if not (l1 and l2):
                tail.next = l1 or l2
                l1 = l1 and l1.next
                l2 = l2 and l2.next
            elif l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        return dummy.next


def test():
    from utils import linkedList, tolist

    solution = Solution()

    a = linkedList([])
    b = linkedList([])
    assert tolist(solution.mergeTwoLists(a, b)) == []

    a = linkedList([2, 4, 6, 8])
    b = linkedList([1, 3, 5, 7])
    assert tolist(solution.mergeTwoLists(a, b)) == [1, 2, 3, 4, 5, 6, 7, 8]

    a = linkedList([])
    b = linkedList([1, 2, 3, 4])
    assert tolist(solution.mergeTwoLists(a, b)) == [1, 2, 3, 4]

    print("self test passed")

if __name__ == '__main__':
    test()
