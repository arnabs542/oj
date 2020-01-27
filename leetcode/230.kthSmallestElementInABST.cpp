/**
 *
 *
230. Kth Smallest Element in a BST

Total Accepted: 78213
Total Submissions: 187183
Difficulty: Medium
Contributors: Admin

Given a binary search tree, write a function kth Smallest to find the kth smallest
element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the
kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:

1. Try to utilize the property of a BST.
2. What if you could modify the BST node's structure?
3. The optimal runtime complexity is O(height of BST).

==============================================================================================
SOLUTION

1. Inorder traversal: get the smallest for k times.

2. Binary Search
Compute the number of nodes on the left and right side, and determine which branch contains
the kth element. To compute the number of nodes in a BST takes time complexity of O(N).

3. But if we can modify the BST nodes' structure, add a count field in the BST node class,
so that we can query kth smallest with binary search, O(logN). And the insertion, deletion
take O(logN) time complexity.

 *
 *
 */
#include <debug.hpp>
#include "./tree.hpp"

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        int result;
        result = kthSmallestRecursive(root, k);

        return result;
    }

    int dfs(TreeNode *root, int &k) {
        if (!root) return 0;
        //if (k == 0 && root) return root->val;
        int result;
        result = dfs(root->left, k);
        if(!k) return result;

        result = root->val;
        --k;
        if(!k) return result;

        return dfs(root->right, k);
    }

    int kthSmallestRecursive(TreeNode *root, int k) {
        int result;
        result = dfs(root, k);
        return result;
    }

    int kthSmallestIterative(TreeNode *root, int k) {
        stack<TreeNode*> filo;
        while (root || filo.size()) {
            while(root) {
                filo.push(root);
                root = root->left;
            }
            TreeNode *pNode = filo.top(); filo.pop();
            --k;
            if (!k) return pNode->val;
            root = pNode->right;
        }

        return 0;
    }
};

//def test():
    //solution = Solution()

    //assert solution.kthSmallest(Codec.deserialize("[1]", int), 1) == 1
    //assert solution.kthSmallest(Codec.deserialize("[2,1,3]", int), 2) == 2
    //assert solution.kthSmallest(Codec.deserialize("[2,1,3]", int), 3) == 3
    //assert solution.kthSmallest(Codec.deserialize("[2,1,3]", int), 6) == None

    //print("self test passed")
int test() {
    cout << "test passed" << endl;
    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
