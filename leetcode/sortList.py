#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
148. Sort List

Total Accepted: 88311
Total Submissions: 327466
Difficulty: Medium
Contributors: Admin

Sort a linked list in O(n log n) time using constant space complexity.

==============================================================================================
SOLUTION:
    1. merge sort: find the middle node, split it into two
    2. heap sort: auxiliary space, not qualified
    3. quick sort: partition by two pointers!
'''
from _utils import linkedList, tolist, ListNode

# Definition for singly-linked list.
# class ListNode(object):

    # def __init__(self, x):
        # self.val = x
        # self.next = None

class Solution(object):

    def sortList(self, head: ListNode, until: ListNode=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sort(head, until=None):
            '''
            Sort the list from head until `until`.
            '''
            if head == until:
                return head
            dummy = ListNode(None)
            dummy.next = head

            # print('before: ', tolist(dummy.next, until))
            # divide: partition
            pivot = head.val
            smaller = dummy
            equal = dummy.next
            while equal.next not in (None, until) and equal.next.val == equal.val:
                equal = equal.next
            prev = equal
            p = prev.next
            while p not in (None, until):
                if p.val < pivot:
                    prev.next = p.next
                    p.next = smaller.next
                    smaller.next = p
                    smaller = p
                # XXX: corner case when equal.next == p
                elif p.val == pivot and equal.next != p:
                    prev.next = p.next
                    p.next = equal.next
                    equal.next = p
                    equal = p
                else:
                    prev = p
                p = prev.next

            # print('after: ', tolist(dummy.next, until), smaller, equal, equal.next)
            # and conquer
            dummy.next = sort(dummy.next, smaller.next)
            equal.next = sort(equal.next, until)
            return dummy.next

        return sort(head)

    # TODO: merge sort version

def test():

    solution = Solution()

    l = []
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == []

    l = [1]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == [1]

    l = [1, 2]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == [1, 2]

    l = [5, 4, 5, 4]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == sorted(l)

    l = [3, 3, 5, 4, 5, 4]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == sorted(l)

    l = [1, 2, 3, 4, 5]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == [1, 2, 3, 4, 5]

    l = [5, 4, 3, 2, 1]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == [1, 2, 3, 4, 5]

    l = [2, 5, 5, 3, 4, 1, 2]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == [1, 2, 2, 3, 4, 5, 5]

    l = [2, 3, 3, 5, 4, 1, 2]
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == [1, 2, 2, 3, 3, 4, 5]

    l = [1] * 2499 + [2] * 2501
    head = linkedList(l)
    head_new = solution.sortList(head)
    l_new = tolist(head_new)
    assert l_new == sorted(l)

    print('self test passed')

if __name__ == '__main__':
    test()
