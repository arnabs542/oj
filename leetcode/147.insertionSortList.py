#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
147. Insertion Sort List

Total Accepted: 100302
Total Submissions: 306443
Difficulty: Medium
Contributor: LeetCode

Sort a linked list using insertion sort.

==============================================================================================
SOLUTION

One of the quotes is
'
FOR GOD'S SAKE, DON'T TRY SORTING A LINKED LIST DURING THE INTERVIEW!
'
http://steve-yegge.blogspot.nl/2008/03/get-that-job-at-google.html

So it might be better to actually copy the values into an array and sort them there.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # return self.insertionSortListTrival(head)
        return self.insertionSortListOpt(head)

    def insertionSortListTrival(self, head):
        # XXX: two dummy variables as sentinel nodes?
        # maybe not, because I don't want to bother to delete it afterward
        dummy = ListNode(float('-inf'))
        dummy.next = None
        # tail = ListNode(float('inf'))
        # dummy.next = tail
        # tail.next = None

        p, tail = head, head
        while p:
            next = p.next
            # insert
            q = dummy
            while True:
                if q.val <= p.val and (q.next and p.val <= q.next.val or not q.next):
                    p.next = q.next
                    q.next = p
                    break
                q = q.next
            p = next

        # remove the sentinel node...
        return dummy.next

    def insertionSortListOpt(self, head):
        dummy = ListNode(float('-inf'))
        dummy.next = None

        p = head
        while p:
            next = p.next
            # insert
            q = dummy
            # XXX: negative condition to reduce nested code
            while q.next and q.next.val < p.val:
                q = q.next
            p.next = q.next
            q.next = p
            p = next

        return dummy.next

    # FIXME: TLE?
    # rewrite with c++, got accepted. TAT
def test():

    from _utils import linkedList, tolist
    solution = Solution()

    l = []
    ll1 = linkedList(l)
    ll2 = solution.insertionSortList(ll1)
    l2 = tolist(ll2)
    assert l2 == []

    l = [1]
    ll1 = linkedList(l)
    ll2 = solution.insertionSortList(ll1)
    l2 = tolist(ll2)
    assert l2 == [1]

    l = [1, 2, 3, 4, 5]
    ll1 = linkedList(l)
    ll2 = solution.insertionSortList(ll1)
    l2 = tolist(ll2)
    assert l2 == [1, 2, 3, 4, 5]

    l = [5, 4, 3, 2, 1]
    head = linkedList(l)
    head_new = solution.insertionSortList(head)
    l_new = tolist(head_new)
    print(l_new)
    assert l_new == [1, 2, 3, 4, 5]

    print("self test passed")

if __name__ == '__main__':
    test()
