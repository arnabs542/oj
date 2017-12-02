#include <memory>
#include <vector>

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

// binary tree node data structure
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x)
        : val(x)
          , left(NULL)
          , right(NULL)
    {
    }

    void print();
    vector<int> inorderTraversal(bool iterative=true);
};
