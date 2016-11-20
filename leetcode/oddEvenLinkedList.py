#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
328. Odd Even Linked List

Total Accepted: 50569
Total Submissions: 122235
Difficulty: Medium
Contributors: Admin

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and
O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def oddEvenList(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        i = 1
        before = prev = dummy
        p = prev.next
        while p:
            if i % 2:
                if before.next == p:
                    prev = p
                else:
                    prev.next = p.next
                    p.next = before.next
                    before.next = p

                before = p
            else:
                prev = p
            i += 1
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

    l = [1, 2, 3, 4, 5]
    head = linkedList(l)
    tolist(head)
    head_new = solution.oddEvenList(head)
    l_new = tolist(head_new)
    assert l_new == [1, 3, 5, 2, 4]

    print('self test passed')

if __name__ == '__main__':
    test()
