#include <memory>
#include <vector>
#include "tree.hpp"

using namespace std;

// linked list node data structure
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x)
        : val(x)
          , next(NULL)
    {
    }
};

struct ListNode* toLinkedList(std::vector<int> nums)
{
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (size_t i = 0; i < nums.size(); ++i) {
        ListNode* node = new ListNode(nums[i]);
        tail->next = node;
        tail = node;
    }
    return dummy.next;
}

std::vector<int> toVector(ListNode* l)
{
    std::vector<int> nums;
    while (l) {
        nums.push_back(l->val);
        l = l->next;
    }
    return nums;
}

    template <typename T>
bool vectorsAreEqual(std::vector<T> v1, std::vector<T> v2)
{
    return v1.size() == v2.size() && std::equal(v1.begin(), v1.end(), v2.begin());
}


