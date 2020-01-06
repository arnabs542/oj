#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
61. Rotate List

Total Accepted: 86707
Total Submissions: 364214
Difficulty: Medium
Contributors: Admin

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        head_new, p, q = head, head, head

        size = 0
        while q:
            size += 1
            q = q.next
        k = k % size if size else k
        if not k:
            return head_new

        q = head
        for _ in range(k):
            if not q:
                return head
            else:
                q = q.next

        while q and q.next:
            p, q = p.next, q.next
        if p and q:
            head_new, p.next, q.next = p.next, None, head

        return head_new

def test():
    solution = Solution()

    print('self test passed')

if __name__ == '__main__':
    test()
