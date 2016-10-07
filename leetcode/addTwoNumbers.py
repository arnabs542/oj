'''
2. Add Two Numbers

Total Accepted: 191198
Total Submissions: 757032
Difficulty: Medium

You are given two linked lists representing two non-negative numbers. The
digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1, node2 = l1, l2
        l3 = None
        carry = 0
        # XXX: mind the carry!
        while node1 or node2 or carry:
            val = carry
            if node1:
                val += node1.val
                node1 = node1.next
            if node2:
                val += node2.val
                node2 = node2.next
            carry = val / 10
            if not l3:
                p3 = ListNode(val % 10)
                l3 = p3
            else:
                p3.next = ListNode(val % 10)
                p3 = p3.next

        return l3
