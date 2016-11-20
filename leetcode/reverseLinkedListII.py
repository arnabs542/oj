#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
92. Reverse Linked List II

Total Accepted: 90413
Total Submissions: 305919
Difficulty: Medium
Contributors: Admin

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

==============================================================================================
SOLUTION:
    1. reverse with First In Last Out order. Also, make use of dummy variables
    2. tip: update pointers in a backward manner
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        before = dummy
        for _ in range(m - 1):
            before = before.next

        rear = before.next
        p = rear.next
        for _ in range(n - m):
            rear.next = p.next
            p.next = before.next
            before.next = p
            p = rear.next

        return dummy.next

def linkedList(l):
        if not l:
            return None
        head = ListNode(l[0])
        p = head
        for i in range(1, len(l)):
            node = ListNode(l[i])
            p.next = node
            p = node

        return head

def tolist(head):
    p = head
    result = []
    while p:
        result.append(p.val)
        p = p.next
    print(result)
    return result

def test():
    solution = Solution()
    l = [1, 2, 3, 4, 5]
    head = linkedList(l)
    tolist(head)
    head_new = solution.reverseBetween(head, 2, 4)
    l_new = tolist(head_new)
    assert l_new == [1, 4, 3, 2, 5]
    head_new = solution.reverseBetween(head, 2, 4)
    assert tolist(head_new) == [1, 2, 3, 4, 5]

    l = [5]
    head = linkedList(l)
    head_new = solution.reverseBetween(head, 1, 1)
    assert tolist(head_new) == [5]

    print('self test passed')

if __name__ == '__main__':
    test()
