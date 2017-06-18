#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
445. Add Two Numbers II

Total Accepted: 19825
Total Submissions: 43006
Difficulty: Medium
Contributor: LeetCode

You are given two non-empty linked lists representing two non-negative integers. The most
significant digit comes first and each of their nodes contain a single digit. Add the two
numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7


==============================================================================================
SOLUTION

The add arithmetic needs to be computed from least to most significant digit. So we may need
to reverse the order, in one way or another.
Reversing the order, means First In Last Out. And one way to do this is with stack, and another
way to do this is the reverse the linked list.

1. Stack
Use two stack to store the numbers in two lists, and build the new list from least to most
significant digit.

Complexity: O(n), O(n)

2. Reverse the output instead
1) Align two lists
2) Build the new list with least significant digit comes first, and each node may contain multiple
digits
3) Compute the carry to make each node contains a single digit
4) Reverse the output list

Complexity: O(n), O(1)

3. Iteratively add carry? Worst case time complexity is O(N²).

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
        # l3 = self.addTwoNumbersStack(l1, l2)
        l3 = self.addTwoNumbersReverse(l1, l2)
        return l3

    def addTwoNumbersStack(self, l1, l2):
        def ll2stack(ll):
            '''
            list to stack
            '''
            s = []
            p = ll
            while p:
                s.append(p.val)
                p = p.next
            return s
        s1, s2 = ll2stack(l1), ll2stack(l2)
        dummy = ListNode(0)
        dummy.next = None
        carry = 0
        while s1 or s2 or carry:
            a = s1 and s1.pop() or 0
            b = s2 and s2.pop() or 0
            carry, c = divmod(a + b + carry, 10)
            node = ListNode(c)
            node.next = dummy.next
            dummy.next = node

        return dummy.next

    def addTwoNumbersReverse(self, l1, l2):
        '''
        reverse output list
        '''
        # TODO: reverse output list
        # function to return the linked list size
        def llsize(p):
            n = 0
            while p:
                n += 1
                p = p.next
            return n

        n1, n2 = llsize(l1), llsize(l2)

        # compute sum, store it in reversed output list
        # each node may contain number larger than 10
        dummy = ListNode(0)
        dummy.next = None
        p, q = l1, l2
        # XXX: dealing with unaligned lists
        while p or q:
            c = 0
            if n1 >= n2:
                c += p.val
                p = p.next
                n1 -= 1
            if n2 > n1:
                c += q.val
                q = q.next
                n2 -= 1
            node = ListNode(c)

            node.next = dummy.next
            dummy.next = node

        # add carry
        prev = dummy
        p = dummy.next
        carry = 0
        while p or carry:
            a = 0
            if p:
                a = p.val
            else:
                p = ListNode(0)
                prev.next = p
            carry, val = divmod(a + carry, 10)
            p.val = val

            prev = p
            p = p.next

        # reverse output linked list
        p = dummy.next
        dummy.next = None

        while p:
            q = p.next
            p.next = dummy.next
            dummy.next = p
            p = q
        return dummy.next

from utils import ListNode, linkedList, tolist

def test():
    solution = Solution()

    l1 = linkedList([])
    l2 = linkedList([1])
    l3 = solution.addTwoNumbers(l1, l2)
    l = tolist(l3)
    assert l == [1]


    l1 = linkedList([])
    l2 = linkedList([])
    l3 = solution.addTwoNumbers(l1, l2)
    l = tolist(l3)
    assert l == []


    l1 = linkedList([])
    l2 = linkedList([1, 2, 3, 4])
    l3 = solution.addTwoNumbers(l1, l2)
    l = tolist(l3)
    assert l == [1, 2, 3, 4]


    l1 = linkedList([9, 9, 9, 9])
    l2 = linkedList([1, 1, 1, 1])
    l3 = solution.addTwoNumbers(l1, l2)
    l = tolist(l3)
    print(l)
    assert l == [1, 1, 1, 1, 0]

    l1 = linkedList([7, 2, 4, 3])
    l2 = linkedList([5, 6, 4])
    l3 = solution.addTwoNumbers(l1, l2)
    l = tolist(l3)
    assert l == [7, 8, 0, 7]

    print("self test passed")

if __name__ == '__main__':
    test()
