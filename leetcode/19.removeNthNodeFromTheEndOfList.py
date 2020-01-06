#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
19. Remove Nth Node From End of List Add to List

Total Accepted: 160007
Total Submissions: 494132
Difficulty: Medium
Contributors: Admin

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

==============================================================================================
SOLUTION

1. Two pointers, the distance between which is n nodes.


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        return self.removeNthFromEndTwoPointers(head, n)

    def removeNthFromEndTwoPointers(self, head, n):
        dummy = ListNode(0) # neutralize the corner case
        dummy.next = head

        p, q = dummy, dummy
        for _ in range(n):
            q = q.next
        while q.next:
            p = p.next
            q = q.next

        p.next = p.next and p.next.next
        return dummy.next

def test():
    from _utils import tolist, linkedList

    solution = Solution()

    assert tolist(solution.removeNthFromEnd(linkedList([]), 0)) == []
    assert tolist(solution.removeNthFromEnd(linkedList([1]), 1)) == []
    assert tolist(solution.removeNthFromEnd(linkedList([1]), 0)) == [1]
    assert tolist(solution.removeNthFromEnd(linkedList([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert tolist(solution.removeNthFromEnd(linkedList([1, 2, 3, 4, 5]), 1)) == [1, 2, 3, 4]
    assert tolist(solution.removeNthFromEnd(linkedList([1, 2, 3, 4, 5]), 5)) == [2, 3, 4, 5]

    print("self test passed")

if __name__ == '__main__':
    test()
