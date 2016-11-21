#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
24. Swap Nodes in Pairs

Total Accepted: 133143
Total Submissions: 361217
Difficulty: Easy
Contributors: Admin

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list,
only nodes itself can be changed.

==============================================================================================
SOLUTION:
    1. dummy pointer
    2. Group SPLIT POINTER
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def swapPairs(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head

        split, prev, p = dummy, dummy, dummy.next
        i = 0
        while p:
            if i % 2 == 0:
                split = prev
                prev = p
            else:
                prev.next = p.next
                p.next = split.next
                split.next = p

            p = prev.next
            i += 1
            pass

        return dummy.next

def test():
    from utils import linkedList, tolist
    solution = Solution()

    l = [1, 2, 3]
    head = linkedList(l)
    tolist(head)
    head_new = solution.swapPairs(head)
    l_new = tolist(head_new)
    assert l_new == [2, 1, 3]

    l = [1, 2, 3, 4]
    head = linkedList(l)
    tolist(head)
    head_new = solution.swapPairs(head)
    l_new = tolist(head_new)
    assert l_new == [2, 1, 4, 3]

    print('self test passed')

if __name__ == '__main__':
    test()
