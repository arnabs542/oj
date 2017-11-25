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

const string leftMark     = "┌───"; // box drawings light Down and Right
const string rightMark    = "└───"; // box drawings light Up and Right
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
    if (root->left) {
        //padding = pos == RIGHT ? innerPadding : (pos == LEFT ? outerPadding : "");
        if (pos == ROOT) {
            padding = "";
        } else {
            padding = pos == RIGHT ? innerPadding : outerPadding;
        }
        printTree(root->left, prefix + padding, LEFT);
    }
    cout << prefix << (pos == LEFT ? leftMark : (pos == RIGHT ? rightMark : ""))
         << root->val << endl;

    if (root->right) {
        //padding = pos == LEFT?innerPadding:(pos == RIGHT?outerPadding:"");
        if (pos == ROOT) {
            padding = "";
        } else {
            padding = pos == LEFT ? innerPadding : outerPadding;
        }
        printTree(root->right, prefix + padding, RIGHT);
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
