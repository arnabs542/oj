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
SOLUTION

First use two pointers(tortoise and hare) as in Cycle Detection problem, where a
fast pointer travels 2 times faster than the slow pointer.

Then find the beginning of the cycle.
----------------------------------------------------------------------------------------------
Circle problem.

Imagine two people A and B are running in a counter-clockwise cycle, while B's speed is twice A's.
Denote the circle perimeter by c, slow one's start point as origin.

-----------------
|               |
|               |
|               |
|               |
|---------------|

If they start at the same point, then they will always meet at the same point.

If the distance between their starting points is a, where will they meet?

Definitions:
c = length of the cycle, if exists.
a = the initial distance between two people, in the cycle.
x = the meet point distance of slow pointer from entry origin.


0----------------
|               |
|               x' = x % c
|               |
|               |
|-------a-------|

So, when they meet, we have equation according to the formula: distance = speed x time.
distance(A has travelled) x 2=  distance(B has travelled)

And since they meet somewhere, denoted by x away from origin.
distance(A travelled) + nc = distance(B), where n = 1, 2, 3, ...

And n corresponds to how many times they have meet.

Assume they meet x away from origin(x may be larger than c).

Then we have
    distance(B) = 2x = x + (c - a) + nc
So, x = (c - a) + nc

Since it's in a circle, period is c, take the modulo, then they meet at:
   x' = x % n = ((c - a) + nc) % c = c - a

In conclusion, they meet at x', where distance from x' to 0, is equal to distance from 0 to a.

0----------------
|               |
|               x' = x % c = c - a
|               |
|               |
|-------a-------|

----------------------------------------------------------------------------------------------
Now, go back to the original problem.

Define the distance from sequence head to cycle entry is h.

(sequence start)         (CIRCLE-START-POINT)
|                            |
(-h)------------------------0----------------
                            |               |
                            |               x' = x % c = c - a (MEET POINT)
                            |               |
                            |               |
                            |-------a-------|
                                    |
       (difference between slow and fast points, when slow enters the cycle)

When the slow pointer enters the cycle 0, it has travelled h, while fast pointer travels 2h.
The difference is:
     2h - h = a + nc.

Since they meet at x', we have x' = c - a, i.e., c - x' = a.
This indicates the distance from x to entry point is equal to the distance from
linked list head to the entry point.

----------------------------------------------------------------------------------------------
Another derivation
2 (h + x' ) = h + x' + nc
So, h + x' = nc, where n = 1, 2, 3, ...
h = nc - x' = (n - 1)c + (c - x') = nc + a, where n = 0, 1, 2, 3, ...
----------------------------------------------------------------------------------------------

And in this iterated function, elements in cycle have period property for arbitrary x:
f(x + nc) = f(x).
So f(x' + h) = f(x' + a + nc) = f(x' + a) = f(c) = f(0).

Which means, f(-h + h) = f(x' + h) = f(0).

Set up another finder pointer a sequence head with speed 1. Move the slow pointer and finder
pointer simultaneously, will eventually meet at the cycle entry!


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
                break

        if fast != slow or fast == slow == dummy: return None
        entry = dummy
        while entry != slow:
            entry, slow = entry.next, slow.next
        return entry

def test():
    solution = Solution()

    print('self test passed')

if __name__ == '__main__':
    test()
