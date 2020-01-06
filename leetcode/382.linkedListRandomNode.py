#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
382. Linked List Random Node

Total Accepted: 20693
Total Submissions: 44684
Difficulty: Medium
Contributors: Admin

Given a singly linked list, return a random node's value from the linked list. Each
node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you
solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal
probability of returning.
solution.getRandom();

==============================================================================================
SOLUTION

Reservoir sampling stochastic process.

Problem:
    Choose k entries from n numbers. Make sure each number is selected with the probability of k/n

Basic idea:
1) Create an array reservoir[0..k-1] and copy first k items to it.
2) Now one by one consider all items from (k+1)th item to nth item.
    a) Generate a random number from 0 to i where i is index of current item in stream[]. Let
the generated random number is j.
    b) If j is in range 0 to k-1, replace reservoir[j] with arr[i]

An intuitive for this algorithm is to use BACKWARD INDUCTION.

Proof:

For i+1th, the probability that it is selected and will replace a number in the reservoir is
Pr(i+1th item is accepted) = P(j is in range 0 to k-1) = k/(i + 1)

For a number in the reservoir before (let's say X), the probability that it keeps staying in the
reservoir is Pr(accepted item is not replaced) = i / (i + 1).

Then, for any ith item, where i > k, the probability that is selected is a joint probability
Pr(ith is selected)
  = Pr(ith is first selected, ith is never replaced)
  = Pr(ith is first selected) * P(ith element is never replaced)
  = Pr(ith is first selected) * P(ith element is never replaced by i+1th) * P(ith element is never replaced by i+2th) * ...
  = (k / i) * (i/(i + 1)) * ((i + 1)/(i + 2)) *....* ((n - 1)/n) = k / n

For any ith item, where i <= k, the joint probability is:
Pr(ith is selected) = 1 * (k / (k + 1)) * ((k + 1) / (k + 2)) * ... * ((n - 1) / n)
= k / n

So, the probability of each number staying in the reservoir is k/n.

'''

import random

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.head
        i, p = 1, node.next if node else None
        while p:
            r = random.randint(0, i)
            if r < 1:
                node = p
            i += 1
            p = p.next
        return node.val




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

def test():
    from _utils import linkedList, tolist

    solution = Solution(linkedList([1, 2, 3]))

    print(solution.getRandom())

    print('self test passed')

if __name__ == '__main__':
    test()
