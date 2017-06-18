/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <unistd.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if (!head) {
            return head;
        }

        ListNode dummy = {0};
        ListNode *p = head;
        ListNode *q = NULL, *next = NULL;
        while(p) {
            q = &dummy;
            while (q->next && q->next->val < p->val) {
                q = q->next;
            }
            next = p->next;
            p->next = q->next;
            q->next = p;
            p = next;
        }

        return dummy.next;
    }
};

int main() {
    return 0;
}
