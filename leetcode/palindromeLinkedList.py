#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
234. Palindrome Linked List Add to List

Total Accepted: 91259
Total Submissions: 285953
Difficulty: Easy
Contributors: Admin

Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

==============================================================================================
SOLUTION

1. To do this in constant space complexity, we can reverse the rear half, and compare it with
the front half.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.isPalindromeReverse(head)

    def isPalindromeReverse(self, head):
        if not head: return True
        dummy = ListNode(0)
        dummy.next = head
        # find the middle node
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next and fast.next.next

        # reverse the rear half
        rear = ListNode(0)
        rear.next = slow.next
        p = rear.next
        while p:
            q = p.next
            p.next = rear.next if p != rear.next else None
            rear.next = p
            p = q

        # compare
        p, q = dummy.next, rear.next
        while q:
            # print(p.val, q.val)
            if p.val != q.val:
                return False
            p, q = p.next, q.next
        return True

def test():

    from utils import linkedList, tolist

    solution = Solution()

    assert solution.isPalindrome(linkedList([1, 2, 3, 4, 3, 2, 1]))
    assert solution.isPalindrome(linkedList([]))
    assert solution.isPalindrome(linkedList([1]))
    assert not solution.isPalindrome(linkedList([1, 2]))
    assert solution.isPalindrome(linkedList([1, 1]))
    assert solution.isPalindrome(linkedList([1, 2, 1]))
    assert solution.isPalindrome(linkedList([1, 2, 3, 3, 2, 1]))

    print("self test passed")

if __name__ == '__main__':
    test()
