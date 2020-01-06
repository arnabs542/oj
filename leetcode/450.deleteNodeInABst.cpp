/*
 *
450. Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

==============================================================================================
SOLUTION

To delete a node, we must find its successor to take its place. As for binary search tree,
the candidate could be largest node that's smaller than target, or the smallest one larger
than the target.

1. Iterative solution
Find the target node.
Find the successor node
Update children pointers of parent node of target node
Update children pointers of successor node
Update children pointers of successor's previous parent node

2. Recursive solution

*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <debug.hpp>
#include "_tree.hpp"
#include "serializeAndDeserializeBinaryTree.hpp"


class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        return _deleteNode(root, key);
    }

    TreeNode* _deleteNode(TreeNode* root, int key) {
        TreeNode *target, *parent, *successor, *pp, *root1 = root;
        target = parent = successor = pp = NULL;
        target = root;
        if (!root) { return NULL; }
        // find target
        while (target && target->val != key) { // find the target node
            parent = target;
            target = target->val > key ? target->left : target->right;
        }
        if (!target)  return root1;
        // find successor
        pp = target;
        successor = target->right;
        while (successor && successor->left)  {
            pp = successor;
            successor = successor->left;
        }
        successor = successor ? successor : target->left;
        // update target's parent:
        if (!parent) { root1 = successor; }
        else if (parent->left == target) { parent->left = successor; }
        else { parent->right = successor; }
        // update successor
        TreeNode *q = successor ? successor->right : NULL;
        if (successor) {
            if (target->left == successor) {
            } else if (target->right == successor) {
                successor->left = target->left;
            } else {
                successor->left = target->left;
                successor->right = target->right;
            }

            target->left = NULL;
            target->right = NULL;
        }
        // last step: update successor's old parent's children reference
        if (pp) {
            if (pp->left == successor) { pp->left = q; }
            else { pp->right = q; }
        }

        return root1;

    }

    // TODO: recursive solution?
};


void test() {
    Solution solution;

    Codec codec;
    string s;
    TreeNode *root = NULL;
    vector<int> result;

    s = "";
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 3);
    assert(codec.serialize(root) == "");

    s = "5,3,6,2,4,null,7";
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 0);
    assert(root->inorderTraversal() == vector<int>({2, 3, 4, 5, 6, 7}));


    s = "5,3,6,2,4,null,7";
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 3);
    root->print();
    assert(root->inorderTraversal() == vector<int>({2, 4, 5, 6, 7}));

    s = "5,3,6,2,4,null,7";
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 5); // delete root
    root->print();
    assert(root->inorderTraversal() == vector<int>({2, 3, 4, 6, 7}));

    s = "5,3,6,2,4,null,7";
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 2);
    root->print();
    assert(root->inorderTraversal() == vector<int>({3, 4, 5, 6, 7}));

    s = "1,#,2,#,3,#,4,#,5"; // right tree
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 1);
    root->print();
    assert(root->inorderTraversal() == vector<int>({2, 3, 4, 5}));

    s = "1,#,2,#,3,#,4,#,5"; // right tree
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 3);
    root->print();
    assert(root->inorderTraversal() == vector<int>({1, 2, 4, 5}));

    s = "8,4,12,2,6,10,14,1,3,5,7,9,11,13,15"; // binary search tree
    root = codec.deserialize(s);
    root->print();
    assert(root->inorderTraversal() == vector<int>(
                {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}));
    root = solution.deleteNode(root, 4);
    //root->print();
    assert(root->inorderTraversal() == vector<int>(
                {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}));
    root = solution.deleteNode(root, 11);
    assert(root->inorderTraversal() == vector<int>(
                {1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15}));
    root = solution.deleteNode(root, 8);
    assert(root->inorderTraversal() == vector<int>(
                {1, 2, 3, 5, 6, 7, 9, 10, 12, 13, 14, 15}));
    root->print();

    s = "0,null,4,2,5,1,3";
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 4);
    assert(root->inorderTraversal() == vector<int>({0, 1, 2, 3, 5,}));

    s = "0,null,4,2,null,1,3";
    root = codec.deserialize(s);
    root = solution.deleteNode(root, 4);
    assert(root->inorderTraversal() == vector<int>({0, 1, 2, 3,}));

    //s = "2,0,33,null,1,25,40,null,null,11,31,34,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,35,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6";
    //root = codec.deserialize(s);
    //root->print();
    //root = solution.deleteNode(root, 33);

    //s = "2,0,34,null,1,25,40,null,null,11,31,36,45,10,18,29,32,35,39,43,46,4,null,12,24,26,30,null,null,null,null,38,null,42,44,null,48,3,9,null,14,22,null,null,27,null,null,37,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,null,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,7,null,16,null,null,20,6";
    //root = codec.deserialize(s);
    //root->print();
    //s = "2,0,34,null,1,25,40,null,null,11,31,35,45,10,18,29,32,null,36,43,46,4,null,12,24,26,30,null,null,null,39,42,44,null,48,3,9,null,14,22,null,null,27,null,null,38,null,41,null,null,null,47,49,null,null,5,null,13,15,21,23,null,28,37,null,null,null,null,null,null,null,null,8,null,null,null,17,19,null,null,null,null,null,null,null,7,null,16,null,null,20,6";
    //root = codec.deserialize(s);
    //root->print();

    cout << "self test passed!" << endl;
}

int main() {
    test();
}
