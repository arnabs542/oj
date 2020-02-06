/**
 *
138. Copy List with Random Pointer


 */

/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */

#include <debug.hpp>

struct RandomListNode {
    int label;
    RandomListNode *next, *random;
    RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
};

class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        RandomListNode *head1 = _copyRandomListAssociateWithNextPointer(head);

        return head1;
    }

    RandomListNode *_copyRandomListAssociateWithNextPointer(RandomListNode *head) {
        RandomListNode dummy = RandomListNode(0);
        RandomListNode *p = NULL, *q = NULL;

        // pass 1, copy and associate
        p = head;
        while (p) {
            q = new RandomListNode(p->label); // new node
            q->next = p->next; // update backward
            p->next = q;

            p = q->next;
        }

        // pass 2, update random pointer
        p = head;
        while (p) {
            q = p->next;
            q->random = p->random ? p->random->next : NULL;

            p = q->next;
        }

        // pass 3,
        RandomListNode *tail = &dummy;
        p = head;
        while (p) {
            q = p->next;

            tail->next = q;
            p->next = q->next;
            q->next = NULL;

            p = p->next;
            tail = tail->next;
        }
        return dummy.next;
    }
};

void test() {
    // TODO: write tests
    cout << "self test needs to be written!" << endl;
}

int main(int argc, char *argv[])
{
    test();

    return 0;
}
