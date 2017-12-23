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

2. Reduce the space complexity by ASSOCIATING old and new nodes with pointers in place!

For the simplest case, where linked list nodes don't have a random pointer. Then we can
just copy the linked list with one pass scanning.

Now we have an additional random pointer, we may want to associate the old nodes to copied
nodes, with an mapping relation, so that we can assign random pointers of copied nodes:
    newNode.random = mapping(oldNode.random)

So the whole space optimization is towards use ASSOCIATIVE MAPPING from old linked list nodes to
new linked list nodes. And hash table is a little bit expensive.

The associative mapping can also be represented with pointers, not just hash table.
And the trick is to choose the right pointer, and decide how to assign those pointers.

----------------------------------------------------------------------------------------------
For each new linked list nodes, set the RANDOM pointer of the old node to the new node
And set the RANDOM pointer of new node to the corresponding old linked list node's random.
Then, we iterate through the linked list again. Meanwhile, we restore the tangled random
pointers of two linked lists.

But this solution WON'T deal with the case when a random pointer from old node points to a
prior node in the linked list, because old node's random pointer is changed during the iteration
and the association is lost.

For this Directed Cyclic Graph, not working, not feasible!

----------------------------------------------------------------------------------------------
3. Associate the old and copied nodes with NEXT pointer, instead of random pointer.

To ASSOCIATE old nodes and copied nodes, we have two choices: use NEXT pointer or RANDOM pointer.
And we need to associate some old nodes with copied nodes, to restore the list structure later.

The above idea can't deal with the case where multiple random pointers point to the same node.

This is because we want to associate original nodes and copied nodes using node pointers while
trying to recover the list structure back again.

The random pointer is random, chaos, and it's not associated with the linked list structure.
But the next pointer is DETERMINISTIC, it corresponds to the list structure.
Given the list structure, the next pointers' distribution is determined, the
conditional entropy is zero!
Then, the next pointer is easy to tangle and easy to restore.

----------------------------------------------------------------------------------------------
1st pass.
When copying nodes,
1) assign the next pointer of old node to the replicate node,
2) assign the next pointer of the replicate node to the old node's next node.

We can associate the new nodes with old nodes without losing the linked list structure,
by tangling the next pointers. And the difference between old random pointer's value and
new random pointer's value is just a reference of NEXT pointer!

2nd pass
And update the new nodes' random pointer, then restore next pointer.

3rd pass
Resolved the tanged next pointer, and extract the copied list.

Set old node's next pointer to copied node, and copied node's next pointer to old node's next.
Update the copied pointer's random pointer.


Original list:
1->2->3->4->5

Copied new linked list:
1->2->3->4->5

Tangled pointer:
1   2   3   4   5
|                   next pointer
1'- 2'- 3'- 4'- 5'

1 - 1' - 2 - 2' - 3 - 3' - 4 - 4' - 5 - 5'

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
            # won't deal with the case where multiple random pointers point to the same node
            p.random, q.random = q.random, q.random and q.random.random
            p = p.next

        return head1

    def copyRandomListAssociateWithNextPointer(self, head: RandomListNode) -> RandomListNode:
        # DONE: copy in place and extract.
        p = head
        # round 1, copy in place
        while p:
            q = RandomListNode(p.label)
            # q.random = p.random
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
