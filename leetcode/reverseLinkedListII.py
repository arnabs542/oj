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
1. Reverse with First In Last Out order. Also, make use of dummy variables
2. Tips: update pointers in a backward manner


----------------------------------------------------------------------------------------------
If one pointer isn't enough, add another one!
If one state isn't enough, add another one!

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
        return self.reverseBetweenLIFO(head, m, n)

    def reverseBetweenLIFO(self, head, m, n):
        '''
        In the simplest situation, we want to reverse a whole linked list, then
        we construct a dummy head, and append nodes in FILO manner.
        But in this scenario, there are trailing nodes after, which we have to keep
        track of. Then we can add another pointer, the rear pointer to keep track of
        those nodes behind the desired segment.

        Reverse with both front and rear pointers.
        '''
        dummy = ListNode(0)
        dummy.next = head

        front = dummy
        for _ in range(m - 1):
            front = front.next

        rear = front.next
        p = rear.next
        for _ in range(n - m):
            rear.next = p.next
            p.next = front.next
            front.next = p
            p = rear.next

        return dummy.next


def test():
    from utils import linkedList, tolist
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
