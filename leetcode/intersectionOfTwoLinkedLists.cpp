/*
 *
 * 160. Intersection of Two Linked Lists
 * Total Accepted: 100621
 * Total Submissions: 333769
 * Difficulty: Easy
 * Contributors: Admin
 * Write a program to find the node at which the intersection of two singly linked lists begins.
 *
 * For example, the following two linked lists:
 *
 * A:          a1 → a2 ↘
 *                        c1 → c2 → c3
 *                        ↗
 * B:     b1 → b2 → b3
 *
 * begin to intersect at node c1.
 *
 * Notes:
 *
 * If the two linked lists have no intersection at all, return null.
 * The linked lists must retain their original structure after the function returns.
 * You may assume there are no cycles anywhere in the entire linked structure.
 * Your code should preferably run in O(n) time and use only O(1) memory.
 *
 *
 * ==============================================================================================
 * SOLUTION:
 *
 * First, we can consider a simple scenario where linked lists A and B have the same length,
 * then we just traverse the two lists simultaneously, and check current nodes equivalency.
 * Now, for arbitrary linked lists, which may have different lengths m and n(say m > n),  we
 * could just adjust our start point to (m - n)th traverse the longer list. Thus, the case is
 * reduced to the former one.
 *
 * Indeed, if m > n, we can start traversing two linked lists with m - n, 0 separately. However,
 * note that m + n = n + m. It means we could traverse the two linked lists like this:
 * Traverse A, till end, start with B. Simultaneously, traverse B, till end, start with A. Then
 * the two pointers traversing share same length of path. The two paths illustrated:
 *
 * ACBC
 * BCAC
 *
 * A..CB...C
 * B...CA..C
 *
 * where len(A) != len(B), but len(A + C + B) == len(B + C + A), so we will find the intersection
 * at the beginning of last C segment. This is a complement situation where we complement one with
 * the other to neutralize imbalanced case.
 */
#include <iostream>

//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x)
    : val(x)
    , next(NULL)
    {
    }
};

class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB)
    {
    if (!(headA && headB)) {
        return NULL;
    }
    ListNode *p = headA, *q = headB;
    while (p != q) {
        p = (p == NULL) ? headB : p->next;
        q = (q == NULL) ? headA : q->next;
    }
    return p;
    }
};
