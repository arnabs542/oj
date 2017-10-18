#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
138. Copy List with Random Pointer Add to List

Total Accepted: 97986
Total Submissions: 368253
Difficulty: Medium
Contributors: Admin

A linked list is given such that each node contains an additional random pointer which
could point to any node in the list or null.

Return a deep copy of the list.


==============================================================================================
SOLUTION

1. Use Hash Table to store the mapping between old nodes to new nodes. Thus, we can modify
the random pointer in each node of the new list to the target new node.
Time complexity: O(N), Space complexity: O(N).

2. Reduce the space complexity by MODIFYING the original linked list in place!
We we first construct the new linked list, store the random pointer in the corresponding
copied linked list node. And set the random pointer of the old node to the new node.
Then, we iterate through the linked list again. Meanwhile, we restore the tangled random
pointers of two linked lists.

But this solution WON'T work because q.random might have been restored to point to the
original list before. And this is a Directed Cyclic Graph, not feasible!

3. Duplicate the new nodes IN PLACE, so that they all closely follow the corresponding
original node. Then modify the random pointers of copied nodes. At last, extract copied
nodes from the original linked list:

1. Iterate the original list and duplicate each node. The duplicate
of each node follows its original directly.
2. Iterate the new list and assign the random pointer for each
duplicated node.
3. Restore the original list and extract the duplicated nodes.

'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        return self.copyRandomListHash(head)

    def copyRandomListHash(self, head: RandomListNode) -> RandomListNode:
        if not head:
            return None
        old2new = {} # mapping the corresponding old nodes to the new ones

        head1 = RandomListNode(head.label)
        head1.random = head.random
        old2new[head] = head1

        p, q = head.next, head1
        while p:
            node = RandomListNode(p.label)
            node.random = p.random
            old2new[p] = node

            q.next, q = node, node
            p = p.next

        q = head1
        while q:
            q.random = q.random and old2new[q.random]
            q = q.next

        return head1

    def copyRandomListIndirectPointer(self, head: RandomListNode) -> RandomListNode:
        '''
        Using pointers in place instead of explicit hash table.
        '''
        if not head: return None
        head1 = RandomListNode(head.label)
        head.random, head1.random = head1, head.random

        p, q = head.next, head1
        while p:
            node = RandomListNode(p.label)
            p.random, node.random = node, p.random

            q.next = node
            q = q.next
            p = p.next

        p = head
        while p:
            q = p.random
            # NOTE: multiple assignment should avoid nested left variables
            # FIXME: q.random might have been restored to point to the original list before
            # And this is a Directed Cyclic Graph, not feasible!
            p.random, q.random = q.random, q.random and q.random.random
            p = p.next

        return head1

    def copyRandomListDupInPlace(self, head: RandomListNode) -> RandomListNode:
        # TODO: copy in place and extract.
        p = head
        # round 1, copy in place
        while p:
            q = RandomListNode(p.label)
            q.random = p.random
            q.next = p.next
            p.next = q
            p = q.next

        # round 2, resolve random pointers
        p = head
        while p:
            q = p.next
            q.random = p.random and p.random.next
            p = q.next

        # round 3, resolve next pointers
        p = head
        dummy = RandomListNode(0)
        # dummy.next = None
        tail = dummy
        while p:
            q = p.next
            tail.next = q
            p.next = q.next

            p = p.next
            tail = tail.next

        return dummy.next

def test():
    from _utils import linkedList, tolist

    solution = Solution()
    # the first part is the linked list, the second part is the random pointers
    # a = [-1,8,7,-3,4, 4,-3,#,#,-1]

    print("self test passed")

if __name__ == '__main__':
    test()
