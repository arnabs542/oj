/**
 *
938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.

================================================================================
SOLUTION

 *
 */

#include <debug.hpp>
#include "tree.hpp"
#include "297.serializeAndDeserializeBinaryTree.hpp"

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
    int rangeSumBST(TreeNode* root, int L, int R) {
        int result;

        result = rangeSumBSTDfs(root, L, R);

        return result;
    }

    int rangeSumBSTDfs(TreeNode* root, int L, int R) {
        if (!root) return 0;
        if (root->val < L) return rangeSumBSTDfs(root->right, L, R);
        else if (root->val > R) return rangeSumBSTDfs(root->left, L, R);
        return root->val + rangeSumBSTDfs(root->left, L, R) + rangeSumBSTDfs(root->right, L, R);
    }
};

int test() {
    //vector<int> nodes;
    //Codec codec;
    TreeNode *root;
    int L, R;
    int output;

    Solution solution;

    string serialized;
    serialized = "10,5,15,3,7,null,18";
    root = Codec::deserialize(serialized);
    L = 7; R = 15;
    output = 32;
    assert(solution.rangeSumBST(root, L, R) == output);

    cout << "test passed" << endl;

    return 0;
}

int main(int argc, char **argv) {
    test();
    return 0;
}
