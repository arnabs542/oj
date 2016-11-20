#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
86. Partition List

Total Accepted: 82799
Total Submissions: 265084
Difficulty: Medium
Contributors: Admin

Given a linked list and a value x, partition it such that all nodes less than x come before
nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

==============================================================================================
SOLUTION:
    A PARTITIONING procedure is similar with partitioning in QUICK SORT. We need to keep a
SPLIT POINT `before` that the elements on the left of it are smaller than pivot. Then we scan the
list, for smaller elements than pivot: append the current node after SPLIT POINT `before` and
update the SPLIT POINT `before` to this node new position.
    While manipulating linked list nodes, one tip is to update pointers BACKWARD its direction.
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        before = prev = dummy
        p = prev.next
        while p:
            if p.val < x:
                if before.next != p:
                    prev.next = p.next
                    p.next = before.next
                    before.next = p
                else:
                    prev = p
                before = p
            else:
                prev = p
            p = prev.next

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

    l = [1, 4, 3, 2, 5, 2]
    head = linkedList(l)
    tolist(head)
    head_new = solution.partition(head, 3)
    l_new = tolist(head_new)
    assert l_new == [1, 2, 2, 4, 3, 5]

    print('self test passed')

if __name__ == '__main__':
    test()
