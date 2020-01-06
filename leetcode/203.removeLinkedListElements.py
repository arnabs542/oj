#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
203. Remove Linked List Elements

Total Accepted: 109761
Total Submissions: 345061
Difficulty: Easy
Contributor: LeetCode

Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

==============================================================================================
SOLUTION


'''

# Definition for singly-linked list.
# class ListNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.next = None

class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        return self.removeElementsPreviousPointer(head, val)
        # return self.removeElementsCopy(head, val)

    def removeElementsCopy(self, head, val):
        pass

    def removeElementsPreviousPointer(self, head, val):
        dummy = ListNode(0)
        dummy.next = head

        prev, p = dummy, None
        while prev:
            p = prev.next
            if p and p.val == val:
                prev.next = p.next
                p.next = None
            else:
                prev = prev.next
        return dummy.next


from _utils import ListNode, linkedList, tolist

def test():
    solution = Solution()

    ll = linkedList([])
    ll = solution.removeElements(ll, 1)
    l = tolist(ll)
    assert l == []

    ll = linkedList([1])
    ll = solution.removeElements(ll, 1)
    l = tolist(ll)
    assert l == []

    ll = linkedList([1, 2])
    ll = solution.removeElements(ll, 2)
    l = tolist(ll)
    assert l == [1]

    ll = linkedList([1, 2, 6, 3, 4, 5, 6])
    ll = solution.removeElements(ll, 6)
    l = tolist(ll)
    assert l == [1, 2, 3, 4, 5]

    ll = linkedList([1, 2, 6, 3, 4, 5, 6])
    ll = solution.removeElements(ll, 1)
    l = tolist(ll)
    assert l == [2, 6, 3, 4, 5, 6]


    print("self test passed")

if __name__ == '__main__':
    test()
