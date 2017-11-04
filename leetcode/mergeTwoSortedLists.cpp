/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include "_utils.hpp"
#include <assert.h>
#include <iostream>

using namespace std;

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		ListNode dummy(0);
		ListNode *tail = &dummy;
		while (l1 && l2) {
			if (l1->val < l2->val) {
				tail->next = l1;
				l1 = l1->next;
			} else {
				tail->next = l2;
				l2 = l2->next;
			}
			tail = tail->next;
		}
		tail->next = l1 ? l1 : l2;
		return dummy.next;
    }
};

void test()
{

	Solution solution;
	ListNode *l1;
	ListNode *l2;
	ListNode *l3 = NULL;

	l1 = toLinkedList(std::vector<int>({}));
	l2 = toLinkedList(std::vector<int>({}));
	l3 = solution.mergeTwoLists(l1, l2);
	assert(vectorsAreEqual<int>(toVector(l3), vector<int>()));

	l1 = toLinkedList(std::vector<int>({}));
	l2 = toLinkedList(std::vector<int>({1, 2, 3,}));
	l3 = solution.mergeTwoLists(l1, l2);
	assert(vectorsAreEqual<int>(toVector(l3), vector<int>({1, 2, 3,})));

	l1 = toLinkedList(std::vector<int>({4}));
	l2 = toLinkedList(std::vector<int>({1, 2, 3,}));
	l3 = solution.mergeTwoLists(l1, l2);
	assert(vectorsAreEqual<int>(toVector(l3), vector<int>({1, 2, 3, 4})));

	l1 = toLinkedList(std::vector<int>({1, 1, 1}));
	l2 = toLinkedList(std::vector<int>({1, 2, 3,}));
	l3 = solution.mergeTwoLists(l1, l2);
	assert(vectorsAreEqual<int>(toVector(l3), vector<int>({1, 1, 1, 1, 2, 3,})));

	cout << "self test passed!" << endl;
}

int main(int argc, char *argv[])
{
	test();
	return 0;
}
