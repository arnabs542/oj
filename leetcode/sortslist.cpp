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
#if DEBUG
                //printf("\np:");
                //for (ListNode *temp = p; temp != q; temp = temp->next)
                //{
                //printf("\t%d", temp->val);
                //}
                //printf("\nq:");
                //for (ListNode *temp = q; temp != NULL; temp = temp->next)
                //{
                //printf("\t%d", temp->val);
                //}
                //printf("\n");
#endif
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
#if DEBUG
                        printf("pp->val:%d,%d > %d\n", pp ? pp->val : 0, p->val, q->val);
#endif
                        if (pp)
                        {
                            pp->next = q;
                            pp = q;
                        }
                        else
                        {
                            head = q;
                            pp = head;
#if DEBUG
                            printf("head->val:%d\n", head->val);
#endif
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
#if DEBUG
                    //printf("pp->val:%d,p->val:%d\n", pp->val, p->val);
#endif
                }//merge two sorted lists
#if DEBUG
                for (ListNode *temp = head; temp; temp = temp->next)
                {
                    printf("%d\t", temp->val);
                }
                printf("\n");
#endif
                nmerges ++;

                pp = p;
                p = q;
                //printf("p= %p\n", p);
            }
            //printf("\n a pass nmeges = %d,l = %d\n",
            //nmerges, l);
            for (ListNode *temp = head; temp; temp = temp->next)
            {
                //printf("%d\t", temp->val);
            }
            //printf("\n");

            if (nmerges == 0)
            {
                break;
            }
            else
            {
                l *= 2;
            }

            //for (ListNode *temp = head; temp; temp = temp->next)
            //{
            //printf("%d\t", temp->val);
            //}
            //printf("\n");
        }//merge along the list

        return head;
    }
};

int main(int argc, char **argv)
{
    int array[] = {4, 19, 14, 5, -3, 1, 8, 5, 11, 15};
    ListNode *sl, *head = NULL, *tail = NULL;
    for (int i = 0; i < 10; i++)
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
