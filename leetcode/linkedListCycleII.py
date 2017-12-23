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

In another word, c - x' = a.

0----------------
|               |
|               x' = x % c = c - a
|               |
|               |
|-------a-------|

----------------------------------------------------------------------------------------------
Now, go back to the original problem.

Definitions:
c = length of the cycle, if exists.
a = the beginning of cycle, with distance a from list start.
x = the meet point distance of slow pointer from entry origin.

    (CIRCLE-START-POINT)
            |
------------a----------------
            |               |
            |               |
            |               |
            |               |
            |-------x-------|
                    |
               (MEET-POINT)


Two pointers travel along the linked list with ones' speed is twice another ones'.
Then when the slow pointer arrives at the entry of circle, the slow pointer is
a' = (2a - a) % c = a % c ahead of slow one.

When they meet at x, we have x = c - a, i.e., c - x = a.
This indicates the distance from x to entry point is equal to the distance from
linked list head to the entry point.

2 (a + x ) = a + x + nc
So, a + x = nc, where n = 1, 2, 3, ...
a = nc - x = (n - 1)c + (c - x)

Final conclusion:
    a = (c - x) % c = c - x + mc, where m = 0, 1, 2, 3,
where c -x is the distance from meet point to linked list cycle entry.

Then two pointers with same speed of 1, starting from the linked list head and cycle entry,
will eventually meet at the linked list entry node!

    (CIRCLE-START-POINT)
            |
------------a----------------
            |               |
            |               |
            |               |
            |               |
            |-------x-------|
                    |
               (MEET-POINT)

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
