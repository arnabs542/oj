#include <debug.hpp>
#include <iostream>
#include "_tree.hpp"

using namespace std;

/**
 * TreeNode methods
 * Inputs
 * - root: root node
 * - prefix: prefix
 * - pos: 0 for root node, 1 for left child , 2 for right child
 */

static const string leftMark     = "└───"; // box drawings light Up and Right
static const string rightMark    = "┌───"; // box drawings light Down and Right
static const string innerPadding = "│   "; // vertical line
static const string outerPadding = "    "; // outer padding

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
    stack<TreeNode*> filo;
    TreeNode *p;

    if (root) filo.push(root);
    while (!filo.empty()) { // while the stack is not empty
        p = filo.top(); // for each stack frame in the stack
        if (p) { // recursive call:  push
            filo.push(p->left);
        } else {   // recursive call returns: base case
            filo.pop();
            if(filo.empty()) break;
            p = filo.top();
            filo.pop();
            result.push_back(p->val);
            filo.push(p->right); // recursive call returns and BACKTRACK: push
        }
    }

}

void postorderTraversalDfs(TreeNode *root, vector<int>& result) {
    if (!root) {
        return;
    }
    postorderTraversalDfs(root->left, result);
    postorderTraversalDfs(root->right, result);
    result.push_back(root->val);
}

/**
 *
 * Define state, the stack frame as a tuple:
 *      tuple<TreeNode*, int>
 * where the integer dimension is the index controlling the search branch: left, child, root
 *
 */
void postorderTraversalIterative(TreeNode *root, vector<int>& result) {
    stack<tuple<TreeNode*, int>> frames;
    TreeNode* p = NULL;
    int i = 0;
    frames.push(make_tuple(root, 0));
    while (frames.size()) {
        tuple<TreeNode*, int> frame = frames.top(); frames.pop();
        p = std::get<0>(frame);
        if (!p)  continue;
        i = std::get<1>(frame);
        if (i == 0) {
            frames.push(make_tuple(p, ++i));
            frames.push(make_tuple(p->left, 0));
        } else if (i == 1) {
            frames.push(make_tuple(p, ++i));
            frames.push(make_tuple(p->right, 0));
        } else {
            result.push_back(p->val);
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

vector<int> TreeNode::postorderTraversal(bool iterative) {
    vector<int> result;
    postorderTraversalDfs(this, result);
    return result;
}

/**
 *
 * Segment tree methods
 *
 */
