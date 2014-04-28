/**
 * Sort List
 *
 * Sort a linked list in O(n log n) time using constant space complexity.
 * The linked list is singly linked.
 */

#include <iostream>
#include <stdio.h>

#define DEBUG 0

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(NULL) {}
};

class Solution
{
public:

    ListNode *sortList(ListNode *head)
    {
        int l = 1, i;
        int psize, qsize;
        int nmerges = 0;
        ListNode *p, *q, *pp, *qp;
        while (1)
        {
            pp = qp = NULL;
            p = head;
            nmerges = 0;
            while (p)
            {
                psize = qsize = l;
                //merge along the list
                for (i = 0, q = p; i < l && q; i++, qp = q, q = q->next);
                if (q == NULL)
                {
                    break;
                }
                for (; psize || (qsize && q);)
                {
                    if (!psize)
                    {
                        qp = q;
                        q = q->next;
                        qsize--;
                    }
                    else if (!qsize || !q)
                    {
                        pp = p;
                        p = p->next;
                        psize--;
                    }
                    else if (p->val > q->val)
                    {
                        //p is bigger than q
                        if (pp)
                        {
                            pp->next = q;
                            pp = q;
                        }
                        else
                        {
                            head = q;
                            pp = head;
                        }

                        qp->next = q->next;
                        q->next = p;

                        q = qp->next;
                        qsize--;

                    }
                    else
                    {
                        //p <= q
                        pp = p;
                        p = p->next;
                        psize--;
                    }
                }//merge two sorted lists

                nmerges ++;

                pp = p;
                p = q;
            }
            if (nmerges == 0)
            {
                break;
            }
            else
            {
                l *= 2;
            }

        }//merge along the list

        return head;
    }
};

int main(int argc, char **argv)
{
    //int array[] = {4, 19, 14, 5, -3, 1, 8, 5, 11, 15};
    int array[] = { -84, 142, 41, -17, -71, 170, 186, 183, -21, -76, 76, 10, 29, 81, 112, -39, -6, -43, 58, 41, 111, 33, 69, 97, -38, 82, -44, -7, 99, 135, 42, 150, 149, -21, -30, 164, 153, 92, 180, -61, 99, -81, 147, 109, 34, 98, 14, 178, 105, 5, 43, 46, 40, -37, 23, 16, 123, -53, 34, 192, -73, 94, 39, 96, 115, 88, -31, -96, 106, 131, 64, 189, -91, -34, -56, -22, 105, 104, 22, -31, -43, 90, 96, 65, -85, 184, 85, 90, 118, 152, -31, 161, 22, 104, -85, 160, 120, -31, 144, 115};
    ListNode *sl, *head = NULL, *tail = NULL;
    for (int i = 0; i < sizeof(array) / sizeof(int); i++)
    {
        //int a = int(i * i * i - 5i * i);
        int a = array[i];
        sl = new ListNode(a);
        if (!head)
        {
            head = tail = sl;
        }
        else
        {
            tail->next = sl;
            tail = sl;
        }
    }

    for (ListNode *p = head; p; p = p->next)
    {
        printf("%d\t", p->val);
    }
    printf("\n");

    Solution s;
    head = s.sortList(head);
    for (ListNode *p = head; p; p = p->next)
    {
        printf("%d\t", p->val);
    }
    printf("\n");
    return 0;
}
