#pragma once

#include <vector>

using namespace std;

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
    vector<int> preorderTraversal(bool iterative=true);
    vector<int> inorderTraversal(bool iterative=true);
    vector<int> postorderTraversal(bool iterative=true);
};
