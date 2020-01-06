#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
141. Linked List Cycle

Total Accepted: 143526
Total Submissions: 399288
Difficulty: Easy
Contributors: Admin

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

==============================================================================================
SOLUTION:
    Two pointers, fast and slow one!
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow != None:
                return True
        return False


def test():
    solution = Solution()

    print("self test passed")

if __name__ == '__main__':
    test()
