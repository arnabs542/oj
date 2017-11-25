/*
 *
 *
 297. Serialize and Deserialize Binary Tree

 Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

 Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

 For example, you may serialize the following tree

 1
 / \
 2   3
 / \
 4   5
 as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Credits:
Special thanks to @Louis1992 for adding this problem and creating all test cases.

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

void assert(bool){}

#include "_type.hpp"
#include "debug.hpp"
//#include <assert.h>
//#include <iostream>
//#include <queue>
//#include <sstream>
//#include <string>

using namespace std;
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root)
    {
        return serializeBfs(root);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data)
    {
        return deserializeBfs(data);
    }

    string serializeBfs(TreeNode* root)
    {
        ostringstream out;

        queue<TreeNode*> q; // queue as search frontier for bfs
        TreeNode* treeNode = NULL;

        if (root) { q.push(root); }

        while (q.size()) { // search frontier queue is not empty
            treeNode = q.front(); // first element of the queue
            q.pop();

            if (treeNode) {
                q.push(treeNode->left); // add connected nodes(children) to search frontier
                q.push(treeNode->right);
            }
            out << (treeNode ? to_string(treeNode->val):"#") << ",";
        }
        string result = out.str();

        // TODO: trim trailing "#"
        string::iterator it = result.end() - 1;
        while (it >= result.begin() && ( *it == ',' || *it == '#')) --it;
        result.erase(it + 1, result.end());

        cout << "serialized tree: " << result << endl;

        return result;
    }

    TreeNode* deserializeBfs(string data)
    {
        cout << "deserialize data: " << data << endl;
        istringstream in(data);
        queue<TreeNode*> q;

        TreeNode *root, *treeNode, *treeNodeNew = NULL;
        string sval;

        root = treeNodeNew = _getNode(in);
        if (treeNodeNew) q.push(treeNodeNew);

        while (q.size()) {
            treeNode = q.front();
            q.pop();
            treeNodeNew = _getNode(in);
            if (treeNodeNew) q.push(treeNodeNew);
            treeNode->left = treeNodeNew;

            treeNodeNew = _getNode(in);
            if (treeNodeNew) q.push(treeNodeNew);
            treeNode->right = treeNodeNew;
        }

        return root;
    }

    TreeNode* _getNode(istringstream& s)
    {
        //if (s.rdbuf()->in_avail() == 0) return NULL; // empty stream
        if (s.eof()) { return NULL; } // empty stream

        string sval;
        //s >> sval;
        getline(s, sval, ',');

        if (sval.compare("") && sval.compare("#") && sval.compare("null") && sval.compare("NULL")) {
            return new TreeNode(stoi(sval));
        }
        return NULL;
    }
};
