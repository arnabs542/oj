#include <debug.hpp>
#include "./_type.hpp"
#include <iostream>

using namespace std;

/**
 *
 * Inputs
 * - root: root node
 * - prefix: prefix
 * - pos: 0 for root node, 1 for left child , 2 for right child
 */

const string leftMark     = "└───"; // box drawings light Up and Right
const string rightMark    = "┌───"; // box drawings light Down and Right
const string innerPadding = "│   "; // vertical line
const string outerPadding = "    "; // outer padding

enum NodeIdx {
    ROOT = 0,
    LEFT,
    RIGHT,
};

void printTree(TreeNode* root, string prefix, NodeIdx pos)
{
    if (root == NULL) {
        cout << "<empty tree>" << endl;
        return;
    }
    string padding;
    if (root->right) {
        //padding = pos == RIGHT ? innerPadding : (pos == LEFT ? outerPadding : "");
        if (pos == ROOT) {
            padding = "";
        } else {
            padding = pos == LEFT ? innerPadding : outerPadding;
        }
        printTree(root->right, prefix + padding, RIGHT);
    }
    cout << prefix << (pos == LEFT ? leftMark : (pos == RIGHT ? rightMark : ""))
         << root->val << endl;

    if (root->left) {
        //padding = pos == LEFT?innerPadding:(pos == RIGHT?outerPadding:"");
        if (pos == ROOT) {
            padding = "";
        } else {
            padding = pos == RIGHT ? innerPadding : outerPadding;
        }
        printTree(root->left, prefix + padding, LEFT);
    }
}

void TreeNode::print()
{
    /*
     *
Used symbols: "┌", "─", "└", "│"
example visualized tree:
            ┌── 31
        ┌── 15
        │   └── 30
    ┌── 7
    │   │   ┌── 29
    │   └── 14
    │       └── 28
    3
    │       ┌── 27
    │   ┌── 13
    │   │   └── 26
    └── 6
        │   ┌── 25
        └── 12
            │   ┌── 49
            └── 24
                └── 48

     */
    cout << "visualize tree: " << this << endl;
    printTree(this, "", ROOT);
    cout << endl;
}

void inorderTraversalDfs(TreeNode *root, vector<int>& result) {
    if (!root) {
        return;
    }
    inorderTraversalDfs(root->left, result);
    result.push_back(root->val);
    inorderTraversalDfs(root->right, result);
}

/*
 * state:
 *
 */
void inorderTraversalIterative(TreeNode *root, vector<int>& result) {
    stack<TreeNode*> nodeStack;
    TreeNode *p;

    if (root) nodeStack.push(root);
    while (!nodeStack.empty()) { // while the stack is not empty
        p = nodeStack.top(); // for each stack frame in the stack
        if (p) { // recursive call:  push
            nodeStack.push(p->left);
        } else {   // recursive call returns: base case
            nodeStack.pop();
            if(nodeStack.empty()) break;
            p = nodeStack.top();
            nodeStack.pop();
            result.push_back(p->val);
            nodeStack.push(p->right); // recursive call returns and BACKTRACK: push
        }
    }

}

vector<int> TreeNode::inorderTraversal(bool iterative) {
    vector<int> result;

    if (iterative) {
        inorderTraversalIterative(this, result);
    } else inorderTraversalDfs(this, result);

    return result;
}
