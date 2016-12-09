#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
142. Linked List Cycle II

Total Accepted: 95151
Total Submissions: 305285
Difficulty: Medium
Contributors: Admin

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

==============================================================================================
SOLUTION:

First use two pointers(tortoise and hare) as in Cycle Detection problem, where a
fast pointer travels 2 times faster than the slow pointer.

Then find the beginning of the cycle.

Definitions:
L = length of the cycle, if exists.
B is the beginning of cycle, M is the meet point distance of slow pointer from B when
slow pointer meets fast pointer.

    (CIRCLE-START-POINT)
            |
------------B----------------
            |               |
            |               |
            |               |
            |               |
            |-------M-------|
                    |
               (MEET-POINT)

Distance(slow) = B + M, Distance(fast) = 2 * Distance(slow) = 2 * (B + M). To let slow
poiner meets fast pointer, only if fast pointer run 1 cycle more than slow pointer.

Distance(fast) - Distance(slow) = nL, n = 1, 2, 3, ...
=> 2 * (B + M) - (B + M)	= nL
=>	B + M = nL
=>	B = nL - M
=>	B = (L - M) + (n - 1)L
=> This means if slow pointer runs B more, it will reaches  (L - M) more.
So at this time, if there's another point2 running from head
=> After B distance, point 2 will meet slow pointer at B, where is the beginning of the cycle.
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def detectCycle(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        fast, slow = dummy, dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                entry = dummy
                while entry != slow:
                    entry, slow = entry.next, slow.next
                pass
                return entry
        return None

def test():
    solution = Solution()

    print('self test passed')

if __name__ == '__main__':
    test()
